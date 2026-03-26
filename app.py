import streamlit as st

# ---------- Custom Styling ----------
st.set_page_config(page_title="Bank App", page_icon="🏦", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🏦 SBI Bank Application</div>', unsafe_allow_html=True)

# ---------- Bank Class ----------
class BankApplication:
    bank_name = 'SBI'

    def __init__(self, name, acc_num, age, mobile_num, balance):
        self.name = name
        self.acc_num = acc_num
        self.age = age
        self.mobile_num = mobile_num
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            return "⚠️ Invalid amount"
        elif amount <= self.balance:
            self.balance -= amount
            return f"✅ Withdrawn ₹{amount}"
        else:
            return "❌ Insufficient Balance"

    def deposit(self, amount):
        if amount <= 0:
            return "⚠️ Invalid amount"
        self.balance += amount
        return f"✅ Deposited ₹{amount}"

    def update_mobile_num(self, new_num):
        self.mobile_num = new_num
        return "📱 Mobile updated successfully"

    def check_balance(self):
        return self.balance


# ---------- Session ----------
if "account" not in st.session_state:
    st.session_state.account = None

# ---------- Sidebar ----------
st.sidebar.title("📌 Menu")
menu = st.sidebar.radio("Navigate", ["Create Account", "Bank Operations"])

# ---------- Create Account ----------
if menu == "Create Account":
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📝 Create New Account")

    name = st.text_input("Name")
    acc_num = st.text_input("Account Number")
    age = st.number_input("Age", min_value=1)
    mobile = st.text_input("Mobile Number")
    balance = st.number_input("Initial Balance", min_value=0)

    if st.button("Create Account"):
        st.session_state.account = BankApplication(
            name, acc_num, age, mobile, balance
        )
        st.success("🎉 Account created successfully!")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Operations ----------
elif menu == "Bank Operations":

    if not st.session_state.account:
        st.warning("⚠️ Please create an account first.")
    else:
        acc = st.session_state.account

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader(f"👋 Welcome, {acc.name}")

        option = st.selectbox(
            "Choose Operation",
            ["Check Balance", "Deposit", "Withdraw", "Update Mobile"]
        )

        # Balance
        if option == "Check Balance":
            if st.button("Check Balance"):
                st.info(f"💰 Your Balance: ₹{acc.check_balance()}")

        # Deposit
        elif option == "Deposit":
            amt = st.number_input("Amount", min_value=1)
            if st.button("Deposit"):
                st.success(acc.deposit(amt))

        # Withdraw
        elif option == "Withdraw":
            amt = st.number_input("Amount", min_value=1)
            if st.button("Withdraw"):
                result = acc.withdraw(amt)
                if "❌" in result:
                    st.error(result)
                else:
                    st.success(result)

        # Update Mobile
        elif option == "Update Mobile":
            new_mobile = st.text_input("New Mobile Number")
            if st.button("Update"):
                st.success(acc.update_mobile_num(new_mobile))

        st.markdown('</div>', unsafe_allow_html=True)