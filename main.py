import pandas as pd


def main():
    # Read in and display the mock dataset from excel
    df = pd.read_excel("SeniorSem_MockData.xlsx", usecols="A:G")

    # 1)
    # Run queries
    query_num = len(df[(df["bound"])])  # Select all the rows where bound is True (bound = true, implies representatives)
    query_den = len(df[(df["offered"]) & (df["channel"] == 1)])  # Select all the rows where offered is true from the representatives
    # Calculate and display the results
    print("\n1) Overall bind rate for all recommendations that were offered (binds can only come from the reps channel)")
    print("Numerator: " + str(query_num))
    print("Denominator: " + str(query_den))
    total = query_num/query_den
    print("The bind rate is: " + str(total) + "\n\n")

    # 2)
    # Run queries
    query_num = len(df[(df["bound"]) & (df["line"] == 'a')])  # Select all the rows where bound is True and line is 'a' (bound = true, implies representatives)
    query_den = len(df[(df["offered"]) & (df["channel"] == 1) & (df["line"] == 'a')])  # Select all the rows where offered is true and line is 'a' from the representatives
    # Calculate and display the results
    print("2) Overall bind rate for all recommendations from line 'a' that were offered (binds can only come from the reps channel)")
    print("Numerator: " + str(query_num))
    print("Denominator: " + str(query_den))
    total = query_num/query_den
    print("The bind rate is: " + str(total) + "\n\n")

    # 3)
    # Run queries
    query_num = len(df[(df["interested"])])  # Select all the rows where interested is True (from both channels)
    query_den = len(df[(df["offered"])])  # Select all the rows where offered is true from both channels
    # Calculate and display the results
    print("3) Overall interested rate for all recommendations that were offered")
    print("Numerator: " + str(query_num))
    print("Denominator: " + str(query_den))
    total = query_num/query_den
    print("The bind rate is: " + str(total) + "\n\n")

    # 4)
    recom_session_count = 0
    session_with_interest = 0
    grouped_df = df.groupby(['interaction_ID'])
    for key, item in grouped_df:
        for i in item.index:
            if item['is_recommended'][i]:
                recom_session_count = recom_session_count + 1
                break
    for key, item in grouped_df:
        for ind in item.index:
            if item['interested'][ind]:
                session_with_interest = session_with_interest + 1
                break
    print("4) Overall interested rate for sessions that contained a recommendation")
    print("Numerator: " + str(session_with_interest))
    print("Denominator: " + str(recom_session_count))
    total = session_with_interest/recom_session_count
    print("The interested rate is: " + str(total) + "\n\n")


if __name__ == '__main__':
    main()
