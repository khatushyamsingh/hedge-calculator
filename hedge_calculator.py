import streamlit as st

def hedge_bet_calculator():
    st.title("Cricket Betting Hedge Calculator")
    st.write("Enter your initial back bet and current lay odds to calculate hedge strategy.")

    back_odds = st.number_input("Back Odds", min_value=1.01, step=0.01)
    back_stake = st.number_input("Back Stake", min_value=1.0, step=1.0)
    lay_odds = st.number_input("Lay Odds", min_value=1.01, step=0.01)

    if st.button("Calculate Hedge"):
        lay_stake = (back_odds * back_stake) / lay_odds
        profit_if_win = round((back_odds - 1) * back_stake - (lay_stake * (lay_odds - 1)), 2)
        profit_if_lose = round(lay_stake - back_stake, 2)

        st.success("To hedge:")
        st.write(f"Lay Stake: ₹{round(lay_stake, 2)}")
        st.write(f"Profit if team wins: ₹{profit_if_win}")
        st.write(f"Profit if team loses: ₹{profit_if_lose}")

if __name__ == '__main__':
    hedge_bet_calculator()
