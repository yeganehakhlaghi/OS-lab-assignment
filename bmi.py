Height = float(input("ghad ra vared konid(m): "))
Weight = float(input("vazn ra vared konid(kg): "))
bmi = Weight/(Height * Height)
if bmi<18.5:
    print(bmi ,'\nUnderweight')
elif bmi<=24.9:
    print(bmi ,'\nNormal')
elif bmi<=29.9:
    print(bmi ,'\nOverweight')
elif bmi<=34.9:
    print(bmi ,'\nObese')
elif bmi>=18.5:
    print(bmi ,'\nExtremeli Obese')

