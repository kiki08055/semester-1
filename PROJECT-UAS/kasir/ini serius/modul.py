def hitungPotongan (total_belanja):
    if total_belanja <= 25000:
        return 0
    elif total_belanja < 30000:
        return 0.05 * total_belanja
    elif total_belanja < 50000:
        return 0.10 * total_belanja
    else:
        return 0.15 * total_belanja

def hitungDiskonPerItem(df, total_belanja, potongan):
    df["Diskon"] = (df["Subtotal"] / total_belanja) * potongan
    return df

def hitung_pajak_total(df):
    df["Pajak (11%)"] = (df["Subtotal"] - df["Diskon"]) * 0.11
    df["Total Akhir"] = (df["Subtotal"] - df["Diskon"] + df["Pajak (11%)"])
    return df
