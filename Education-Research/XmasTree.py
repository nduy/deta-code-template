'''
Deealta-code-template
'''

def holidaybush(n):
    for i in range(n):
        print(("🟢" * (i * 2 + 1)).center(n * 2 - 1))

if __name__=='__main__':
  print("Hello, World!");
  holidaybush(20)