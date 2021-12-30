import pandas as pd

def main():
    file_base = "MSCallGraph_"
    unique_rpcid = []
    for i in range(145):
        print("Parsed file", i)
        filename = file_base + str(i) + ".csv"
        df = pd.read_csv(filename)
        unique_rpcid += df['rpcid'].unique().tolist()
    unique_rpcid = set(unique_rpcid)
    with open('unique_rpcid.csv', 'w+') as outf:
        for rpcid in unique_rpcid:
            outf.write(str(rpcid) + "\n")

if __name__ == '__main__':
    main()
