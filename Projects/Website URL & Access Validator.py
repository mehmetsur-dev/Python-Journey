# Website URL & Access Validator

# Step 1: Clean up & Fallback
user_input_url = ""

if not user_input_url:
    final_url = "https://mywebsite.com"  # Safe fallback so the script doesn't break
else:
    final_url = user_input_url

# Step 2: Secure check
is_secure = final_url.startswith('https://')
print(f"Is secure: {is_secure}")

# Step 3: Permissions
user_role = 'Admin'
is_banned = False

if user_role == 'Admin' and not is_banned:
    print('Full access')
else:
    print('Access Denied')

# Step 4: Identity vs Equality
protocols_supported = ["http", "https"]
protocols_allowed = ["http", "https"]

print(protocols_allowed == protocols_supported)  # True (Same values)
print(protocols_allowed is protocols_supported)   # False (Different memory locations)