
def exit(fname,para=None):
    print("Do you want to exit?\nFor 'yes' type 1 and for 'no' type 0 ")
    decision=int(input())
    match decision:
        case 1:
            print("Thank you!!!")
            return 0
        case 0:
            if para is not None:
                fname(para)
            else:
                fname()
        case _:
            exit()

