
def foo(science):
    for record in open('sslc1.txt'):
        fields = record.split(';')
        region_code = fields[0].strip()

        score_str = fields[6].strip()
        score = int(score_str) if score_str != 'AA' \
                               else 0

        if score > 90:
            science[region_code] += 1

def bar():
    science = {}
    science = foo(science)
    pie(science.values(), labels=science.keys())
    savefig('science.png')

if __name__ == '__main__':
    bar()

