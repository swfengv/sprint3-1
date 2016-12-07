def parseTxt(name):

    f = open(name,"r")
    st = f.readline()
    result = []

    while st != "":
        if st[:st.find(",")] not in result:

            uName = st[:st.find(",")].strip()

            st = st[st.find(",") + 1:]
            password = st[:st.find(",")].strip()

            st = st[st.find(",") + 1:]
            accnt = st.strip()

            user = User()
            user.name = uName
            user.password = password
            user.aType = accnt

            user.put()
            result.append(user)
            st = f.readline()

    return result
