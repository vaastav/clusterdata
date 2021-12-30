import pandas as pd

def main():
    file_base = "MSResource_"
    unique_ms = []
    unique_instances = []
    for i in range(12):
        print("Parsed file", i)
        filename = file_base + str(i) + ".csv"
        df = pd.read_csv(filename)
        unique_ms += df['msname'].unique().tolist()
        unique_instances += df['msinstanceid'].unique().tolist()
    unique_ms = set(unique_ms)
    unique_instances = set(unique_instances)
    with open('unique_ms.csv', 'w+') as outf:
        outf.write('\n'.join(unique_ms))
    with open('unique_instances.csv', 'w+') as outf:
        outf.write('\n'.join(unique_instances))

if __name__ == '__main__':
    main()
