kmp = float(input('Quantos kilometros foram percorridos? : '))
da = int(input('Voce quantos dias foram alugados? : '))
kmr = kmp * 0.15
dap = da * 60
soma = dap + kmr

print(f'Voce deve pagar {soma:.2f}R$ por dias alugados e kilometros rodados')
