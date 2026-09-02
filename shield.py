# shield.py
# Privacy Shield
# শুধু Shield / Privacy logic এখানে থাকবে।
# UI বা Button-এর কাজ এখানে থাকবে না.

from urllib.parse import urlparse


# ==========================================================
# 1. Sensitive Android permissions
# ==========================================================

BLOCKED_PERMISSIONS = {
    "android.permission.ACCESS_FINE_LOCATION",
    "android.permission.ACCESS_COARSE_LOCATION",

    "android.permission.CAMERA",
    "android.permission.RECORD_AUDIO",

    "android.permission.READ_CONTACTS",
    "android.permission.WRITE_CONTACTS",

    "android.permission.READ_SMS",
    "android.permission.SEND_SMS",

    "android.permission.READ_CALL_LOG",
    "android.permission.WRITE_CALL_LOG",

    "android.permission.READ_PHONE_STATE",
    "android.permission.READ_PHONE_NUMBERS",
    "android.permission.CALL_PHONE",

    "android.permission.BLUETOOTH",
    "android.permission.BLUETOOTH_CONNECT",
    "android.permission.BLUETOOTH_SCAN",

    "android.permission.ACCESS_BACKGROUND_LOCATION",
}


# শুধুমাত্র Internet permission-এর policy
ALLOWED_PERMISSIONS = {
    "android.permission.INTERNET"
}


def is_permission_blocked(permission):
    """Sensitive Android permission blocked কিনা পরীক্ষা করে."""
    return permission in BLOCKED_PERMISSIONS


def get_allowed_permissions():
    """অ্যাপের অনুমোদিত permission ফেরত দেয়."""
    return set(ALLOWED_PERMISSIONS)


# ==========================================================
# 2. Sensitive device information
# ==========================================================

BLOCKED_DEVICE_DATA = {
    "imei",
    "imsi",
    "android_id",
    "device_id",
    "serial",
    "phone_number",

    "location",
    "gps",

    "contacts",
    "sms",
    "call_log",

    "camera",
    "microphone",

    "bluetooth",

    "wifi_ssid",
    "wifi_bssid",

    "advertising_id",
}


def is_device_data_blocked(data_name):
    """
    Sensitive device information-এর access
    Shield policy অনুযায়ী blocked কিনা পরীক্ষা করে.
    """

    if not isinstance(data_name, str):
        return True

    return data_name.lower().strip() in BLOCKED_DEVICE_DATA


# ==========================================================
# 3. Network protection
# ==========================================================

# কোনো external server manually allow করা হচ্ছে না।
ALLOWED_DOMAINS = set()


def is_secure_url(url):
    """
    শুধু HTTPS URL গ্রহণ করে।
    """

    try:
        parsed = urlparse(url)

        return (
            parsed.scheme.lower() == "https"
            and bool(parsed.hostname)
        )

    except Exception:
        return False


def is_domain_allowed(url):
    """
    বর্তমানে কোনো domain allow করা নেই।

    পরে নিজের অনুমোদিত API দরকার হলে এখানে
    domain policy যোগ করা যাবে।
    """

    return False


def can_connect(url):
    """
    Network connection-এর আগে Shield check।

    বর্তমানে:
    - HTTPS না হলে = BLOCK
    - কোনো domain allow করা নেই = BLOCK

    তাই এই function-এর মাধ্যমে কোনো external
    server connection অনুমোদিত নয়।
    """

    if not is_secure_url(url):
        return False

    if not is_domain_allowed(url):
        return False

    return True


# ==========================================================
# 4. Web / Fingerprint policy
# ==========================================================

BLOCKED_WEB_FEATURES = {
    "geolocation",
    "camera",
    "microphone",
    "notifications",
    "clipboard-read",
    "clipboard-write",
}


def is_web_feature_blocked(feature):
    """Web feature blocked কিনা পরীক্ষা করে."""

    if not isinstance(feature, str):
        return True

    return feature.lower().strip() in BLOCKED_WEB_FEATURES


# ==========================================================
# 5. Fingerprint-related policy
# ==========================================================

BLOCKED_FINGERPRINT_FEATURES = {
    "canvas",
    "webgl",
    "webrtc",
    "navigator_device_memory",
    "navigator_hardware_concurrency",
    "navigator_platform",
    "navigator_user_agent",
    "screen_information",
    "timezone",
    "language",
}


def is_fingerprint_feature_blocked(feature):
    """
    Fingerprint-related feature ব্যবহার করার আগে
    policy check করার জন্য।
    """

    if not isinstance(feature, str):
        return True

    return feature.lower().strip() in BLOCKED_FINGERPRINT_FEATURES


# ==========================================================
# 6. Privacy status
# ==========================================================

def privacy_status():
    """
    Shield-এর বর্তমান policy status।
    """

    return {
        "location": "BLOCKED",
        "camera": "BLOCKED",
        "microphone": "BLOCKED",
        "contacts": "BLOCKED",
        "sms": "BLOCKED",
        "phone_state": "BLOCKED",
        "imei": "BLOCKED",
        "imsi": "BLOCKED",
        "android_id": "BLOCKED",
        "serial": "BLOCKED",
        "bluetooth": "BLOCKED",

        "canvas": "BLOCKED",
        "webgl": "BLOCKED",
        "webrtc": "BLOCKED",
        "geolocation": "BLOCKED",

        "https_only": True,
        "external_servers": "BLOCKED",
    }


# ==========================================================
# 7. Master Shield
# ==========================================================

SHIELD_ENABLED = True


def shield_enabled():
    """Shield চালু আছে কিনা ফেরত দেয়."""
    return SHIELD_ENABLED
