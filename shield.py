# shield.py
#
# Privacy Shield
# এই ফাইলে শুধু privacy/security related logic থাকবে।
# UI বা button-এর কোনো code এখানে থাকবে না.

from urllib.parse import urlparse


# --------------------------------------------------
# 1. Sensitive Android permissions
# --------------------------------------------------

# অ্যাপের প্রয়োজন নেই এমন sensitive permission-এর তালিকা।
# আমরা এগুলোর জন্য permission request করব না।
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
}


def get_allowed_permissions():
    """
    অ্যাপের জন্য প্রয়োজনীয় permission-এর তালিকা।
    Privacy-first mode-এ INTERNET ছাড়া কিছু রাখা হচ্ছে না।
    """
    return {
        "android.permission.INTERNET"
    }


def is_permission_blocked(permission):
    """কোনো sensitive permission Shield দ্বারা blocked কি না।"""
    return permission in BLOCKED_PERMISSIONS


# --------------------------------------------------
# 2. Device information protection
# --------------------------------------------------

PROTECTED_DEVICE_DATA = {
    "imei",
    "imsi",
    "android_id",
    "serial",
    "phone_number",
    "location",
    "contacts",
    "sms",
    "call_log",
    "camera",
    "microphone",
    "bluetooth",
}


def is_device_data_protected(data_name):
    """
    Sensitive device data access করার আগে এই check ব্যবহার করা যাবে।
    """
    return str(data_name).lower() in PROTECTED_DEVICE_DATA


# --------------------------------------------------
# 3. Network server allowlist
# --------------------------------------------------

# এখানে শুধুমাত্র যেসব domain-এ অ্যাপ network request
# করতে পারবে সেগুলো রাখা যাবে।
#
# নিজের API ব্যবহার করলে এখানে নিজের domain যোগ করবে।
ALLOWED_DOMAINS = {
    # "api.example.com",
}


def is_domain_allowed(url):
    """
    URL-এর domain allowlist-এর মধ্যে আছে কি না পরীক্ষা করে।
    """

    try:
        parsed = urlparse(url)

        if parsed.scheme not in ("https",):
            return False

        hostname = parsed.hostname

        if not hostname:
            return False

        hostname = hostname.lower()

        return (
            hostname in ALLOWED_DOMAINS
            or any(
                hostname.endswith("." + domain)
                for domain in ALLOWED_DOMAINS
            )
        )

    except Exception:
        return False


# --------------------------------------------------
# 4. HTTPS only
# --------------------------------------------------

def is_secure_url(url):
    """শুধু HTTPS URL অনুমোদন করে।"""

    try:
        return urlparse(url).scheme.lower() == "https"
    except Exception:
        return False


# --------------------------------------------------
# 5. Privacy check
# --------------------------------------------------

def privacy_check():
    """
    Shield-এর বর্তমান policy এক জায়গা থেকে পরীক্ষা করার জন্য।
    """

    return {
        "internet": True,
        "location": False,
        "camera": False,
        "microphone": False,
        "contacts": False,
        "sms": False,
        "phone_state": False,
        "imei": False,
        "android_id": False,
        "serial": False,
        "bluetooth": False,
        "https_only": True,
    }
