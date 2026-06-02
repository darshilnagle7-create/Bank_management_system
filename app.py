import json
import random
import string
from pathlib import Path
import streamlit as st

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="NexaBank",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}

/* Background */
.stApp {
    background: #0a0a0f;
    color: #e8e4dc;
}

/* Hide default streamlit elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 4rem; max-width: 720px; }

/* ── Hero Banner ── */
.hero {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    border: 1px solid rgba(99, 179, 237, 0.2);
    border-radius: 20px;
    padding: 2.5rem 2rem 2rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(99,179,237,0.15) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-title {
    font-size: 2.8rem;
    font-weight: 800;
    color: #e8e4dc;
    letter-spacing: -1px;
    margin: 0 0 0.3rem;
}
.hero-title span { color: #63b3ed; }
.hero-sub {
    font-family: 'DM Mono', monospace;
    font-size: 0.8rem;
    color: rgba(232,228,220,0.45);
    letter-spacing: 3px;
    text-transform: uppercase;
}

/* ── Section Card ── */
.section-card {
    background: #111118;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 1.8rem 1.6rem;
    margin-bottom: 1.2rem;
}
.section-title {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #63b3ed;
    margin-bottom: 1rem;
}

/* ── Stat cards ── */
.stat-row { display: flex; gap: 1rem; margin-bottom: 1.2rem; }
.stat-card {
    flex: 1;
    background: #16161f;
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px;
    padding: 1rem 1.2rem;
}
.stat-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    color: rgba(232,228,220,0.4);
    letter-spacing: 2px;
    text-transform: uppercase;
}
.stat-value {
    font-size: 1.5rem;
    font-weight: 700;
    color: #e8e4dc;
    margin-top: 0.2rem;
}
.stat-value.green { color: #68d391; }
.stat-value.blue  { color: #63b3ed; }

/* ── Inputs ── */
div[data-baseweb="input"] input,
div[data-baseweb="select"] > div {
    background: #16161f !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 10px !important;
    color: #e8e4dc !important;
    font-family: 'DM Mono', monospace !important;
}
div[data-baseweb="input"] input:focus {
    border-color: #63b3ed !important;
    box-shadow: 0 0 0 2px rgba(99,179,237,0.15) !important;
}

/* Labels */
label, .stTextInput label, .stNumberInput label, .stSelectbox label {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    letter-spacing: 1px !important;
    color: rgba(232,228,220,0.6) !important;
    text-transform: uppercase !important;
}

/* ── Primary Button ── */
.stButton > button {
    background: linear-gradient(135deg, #2b6cb0, #3182ce) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    padding: 0.6rem 1.8rem !important;
    transition: all 0.2s ease !important;
    width: 100% !important;
    font-size: 0.9rem !important;
    text-transform: uppercase !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #3182ce, #4299e1) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(99,179,237,0.25) !important;
}

/* ── Alerts ── */
.stSuccess > div {
    background: rgba(104, 211, 145, 0.08) !important;
    border: 1px solid rgba(104, 211, 145, 0.3) !important;
    border-radius: 10px !important;
    color: #68d391 !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.85rem !important;
}
.stError > div {
    background: rgba(252, 129, 74, 0.08) !important;
    border: 1px solid rgba(252, 129, 74, 0.3) !important;
    border-radius: 10px !important;
    color: #fc814a !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.85rem !important;
}
.stWarning > div {
    background: rgba(246, 224, 94, 0.08) !important;
    border: 1px solid rgba(246, 224, 94, 0.3) !important;
    border-radius: 10px !important;
    color: #f6e05e !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.85rem !important;
}
.stInfo > div {
    background: rgba(99, 179, 237, 0.08) !important;
    border: 1px solid rgba(99, 179, 237, 0.3) !important;
    border-radius: 10px !important;
    color: #63b3ed !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.85rem !important;
}

/* ── Selectbox ── */
div[data-baseweb="select"] {
    font-family: 'Syne', sans-serif !important;
}

/* ── Divider ── */
hr { border-color: rgba(255,255,255,0.06) !important; }

/* ── Account badge ── */
.acc-badge {
    display: inline-block;
    background: rgba(99,179,237,0.1);
    border: 1px solid rgba(99,179,237,0.3);
    border-radius: 8px;
    padding: 0.3rem 0.8rem;
    font-family: 'DM Mono', monospace;
    font-size: 0.85rem;
    color: #63b3ed;
    letter-spacing: 2px;
    margin-top: 0.4rem;
    word-break: break-all;
}

/* Detail table */
.detail-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.7rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    font-size: 0.9rem;
}
.detail-row:last-child { border-bottom: none; }
.detail-key {
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: rgba(232,228,220,0.4);
}
.detail-val {
    font-weight: 600;
    color: #e8e4dc;
}
.balance-val { color: #68d391; font-size: 1.1rem; }
</style>
""", unsafe_allow_html=True)

# ─── Data Layer ─────────────────────────────────────────────────────────────
DATABASE = "nexa_database.json"

def load_data():
    if Path(DATABASE).exists():
        with open(DATABASE) as f:
            return json.loads(f.read())
    return []

def save_data(data):
    with open(DATABASE, "w") as f:
        f.write(json.dumps(data, indent=2))

def generate_account_no():
    alpha = random.choices(string.ascii_uppercase, k=6)
    num   = random.choices(string.digits, k=6)
    acc   = alpha + num
    random.shuffle(acc)
    return "NX-" + "".join(acc)

def find_user(data, accno, pin):
    matches = [u for u in data if u["AccountNo."] == accno and u["pin"] == int(pin)]
    return matches[0] if matches else None

# ─── Hero ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-title">Nexa<span>Bank</span></div>
  <div class="hero-sub">Digital Banking Terminal · v2.0</div>
</div>
""", unsafe_allow_html=True)

# ─── Stats ───────────────────────────────────────────────────────────────────
data = load_data()
total_accounts = len(data)
total_deposits = sum(u.get("balance", 0) for u in data)

st.markdown(f"""
<div class="stat-row">
  <div class="stat-card">
    <div class="stat-label">Total Accounts</div>
    <div class="stat-value blue">{total_accounts}</div>
  </div>
  <div class="stat-card">
    <div class="stat-label">Total Deposits</div>
    <div class="stat-value green">₹ {total_deposits:,.2f}</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── Navigation ──────────────────────────────────────────────────────────────
OPERATIONS = [
    "🆕  Create Account",
    "💳  Deposit Money",
    "💸  Withdraw Money",
    "👁  View Account Details",
    "✏️  Update Details",
    "🗑  Delete Account",
]

st.markdown('<div class="section-title">Select Operation</div>', unsafe_allow_html=True)
op = st.selectbox("", OPERATIONS, label_visibility="collapsed")

st.markdown("<hr>", unsafe_allow_html=True)

# ─── Operations ──────────────────────────────────────────────────────────────

# ── 1. Create Account ────────────────────────────────────────────────────────
if op == OPERATIONS[0]:
    st.markdown('<div class="section-title">Open New Account</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        name  = st.text_input("Full Name")
        age   = st.number_input("Age", min_value=1, max_value=120, step=1)
    with col2:
        email = st.text_input("Email Address")
        pin   = st.text_input("4-Digit PIN", type="password", max_chars=4)

    if st.button("Open Account"):
        if not all([name, email, pin]):
            st.error("Please fill in all fields.")
        elif not pin.isdigit() or len(pin) != 4:
            st.error("PIN must be exactly 4 digits.")
        elif age < 12:
            st.error("Minimum age to open an account is 12 years.")
        else:
            data = load_data()
            acc_no = generate_account_no()
            data.append({
                "name":       name,
                "age":        int(age),
                "email":      email,
                "AccountNo.": acc_no,
                "pin":        int(pin),
                "balance":    0
            })
            save_data(data)
            st.success(f"✅ Account created successfully!")
            st.markdown(f"""
            <div style="margin-top:1rem;">
              <div class="stat-label">Your Account Number</div>
              <div class="acc-badge">{acc_no}</div>
              <div style="font-family:'DM Mono',monospace;font-size:0.72rem;color:rgba(232,228,220,0.4);margin-top:0.5rem;">
                Save this number — you'll need it for all transactions.
              </div>
            </div>
            """, unsafe_allow_html=True)

# ── 2. Deposit ───────────────────────────────────────────────────────────────
elif op == OPERATIONS[1]:
    st.markdown('<div class="section-title">Deposit Funds</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        accno = st.text_input("Account Number")
    with col2:
        pin   = st.text_input("PIN", type="password", max_chars=4)

    amount = st.number_input("Deposit Amount (₹)", min_value=1, step=100)

    if st.button("Deposit"):
        if not accno or not pin:
            st.error("Please enter account number and PIN.")
        else:
            data = load_data()
            user = find_user(data, accno.strip(), pin)
            if not user:
                st.error("Invalid account number or PIN.")
            elif amount <= 0:
                st.warning("Enter a valid amount.")
            else:
                user["balance"] += amount
                save_data(data)
                st.success(f"₹ {amount:,.2f} deposited. New balance: ₹ {user['balance']:,.2f}")

# ── 3. Withdraw ──────────────────────────────────────────────────────────────
elif op == OPERATIONS[2]:
    st.markdown('<div class="section-title">Withdraw Funds</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        accno = st.text_input("Account Number")
    with col2:
        pin   = st.text_input("PIN", type="password", max_chars=4)

    amount = st.number_input("Withdraw Amount (₹)", min_value=1, step=100)

    if st.button("Withdraw"):
        if not accno or not pin:
            st.error("Please enter account number and PIN.")
        else:
            data = load_data()
            user = find_user(data, accno.strip(), pin)
            if not user:
                st.error("Invalid account number or PIN.")
            elif amount > user["balance"]:
                st.error(f"Insufficient funds. Available: ₹ {user['balance']:,.2f}")
            else:
                user["balance"] -= amount
                save_data(data)
                st.success(f"₹ {amount:,.2f} withdrawn. Remaining balance: ₹ {user['balance']:,.2f}")

# ── 4. View Details ──────────────────────────────────────────────────────────
elif op == OPERATIONS[3]:
    st.markdown('<div class="section-title">Account Details</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        accno = st.text_input("Account Number")
    with col2:
        pin   = st.text_input("PIN", type="password", max_chars=4)

    if st.button("View Details"):
        if not accno or not pin:
            st.error("Please enter account number and PIN.")
        else:
            data = load_data()
            user = find_user(data, accno.strip(), pin)
            if not user:
                st.error("Invalid account number or PIN.")
            else:
                labels = {
                    "name":       "Full Name",
                    "age":        "Age",
                    "email":      "Email",
                    "AccountNo.": "Account No.",
                    "balance":    "Balance",
                }
                rows_html = ""
                for key, label in labels.items():
                    val = user.get(key, "—")
                    val_class = "balance-val" if key == "balance" else "detail-val"
                    display = f"₹ {val:,.2f}" if key == "balance" else val
                    rows_html += f"""
                    <div class="detail-row">
                      <span class="detail-key">{label}</span>
                      <span class="{val_class}">{display}</span>
                    </div>"""
                st.markdown(f'<div class="section-card">{rows_html}</div>', unsafe_allow_html=True)

# ── 5. Update Details ────────────────────────────────────────────────────────
elif op == OPERATIONS[4]:
    st.markdown('<div class="section-title">Update Account Info</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        accno = st.text_input("Account Number")
    with col2:
        pin   = st.text_input("Current PIN", type="password", max_chars=4)

    if accno and pin:
        data = load_data()
        user = find_user(data, accno.strip(), pin)
        if user:
            st.info("Leave fields blank to keep current values.")
            new_name  = st.text_input("New Name",  placeholder=user["name"])
            new_email = st.text_input("New Email", placeholder=user["email"])
            new_pin   = st.text_input("New PIN (4 digits)", type="password", max_chars=4)

            if st.button("Update"):
                if new_name.strip():
                    user["name"] = new_name.strip()
                if new_email.strip():
                    user["email"] = new_email.strip()
                if new_pin.strip():
                    if not new_pin.isdigit() or len(new_pin) != 4:
                        st.error("New PIN must be exactly 4 digits.")
                        st.stop()
                    user["pin"] = int(new_pin)
                save_data(data)
                st.success("Account details updated successfully.")
        else:
            st.error("Invalid account number or PIN.")

# ── 6. Delete Account ────────────────────────────────────────────────────────
elif op == OPERATIONS[5]:
    st.markdown('<div class="section-title">Close Account</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        accno = st.text_input("Account Number")
    with col2:
        pin   = st.text_input("PIN", type="password", max_chars=4)

    confirm = st.checkbox("I understand this action is irreversible")

    if st.button("Delete Account"):
        if not accno or not pin:
            st.error("Please enter account number and PIN.")
        elif not confirm:
            st.warning("Please confirm by checking the box above.")
        else:
            data = load_data()
            user = find_user(data, accno.strip(), pin)
            if not user:
                st.error("Invalid account number or PIN.")
            else:
                data.remove(user)
                save_data(data)
                st.success("Account successfully closed.")

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style="margin-top:3rem;text-align:center;font-family:'DM Mono',monospace;
            font-size:0.68rem;letter-spacing:2px;color:rgba(232,228,220,0.2);
            text-transform:uppercase;">
  NexaBank · Secure Digital Banking · 2025
</div>
""", unsafe_allow_html=True)