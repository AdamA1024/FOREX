def get_his_data_filename(pair, granlarity):
    return f"data/{pair}_{granlarity}.pkl"

def get_instruments_data_filename():
    return "instrument.pkl"

if __name__ == "__main__":
    print(get_his_data_filename("EUR_USD", "M1"))
    print(get_instruments_data_filename())