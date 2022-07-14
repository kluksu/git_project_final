from random import *
import statistics


" תמיר! אנא שים לב שמימשתי פונקציה שמג'נרטת מילונים של אנשים ובונה את  data_set" \
" לכן כאשר מריצים את MAIN " \
"המספר הראשון שמזינים הוא מספר האנשים שאתה רוצה לייצר ולאחר מכן את המסננים " \
"כמו כן שים לב שהפונקציות find_median_avarage וprint_values_above הן אינן תלויות אחת בשניה," \
" אם סיננת לפי גיל אז החציון והממוצע ישארו לכלל האוכלוסיה (אלו ההוראות - הפונקציה רק מדפיסה ולא מחזירה)  "

data_set={}
def add_people(id: int,name: str,age : int,sex : str):
    """
     add items to data_set
    :param id:
    :param name:
    :param age:
    :param sex:
    :return:
    """

    data_set[id]={"name":name,"age":age,"sex":sex}
def people_generator(num_of_people:int):

 for people in range(0,num_of_people,1):
    age=randint(1, 100)
    id=randint(3000000000, 4000000000)
    sex="male" if  random()<0.5 else "female"
    name=""
    num_of_letters=range(0,randint(2, 8),1)
    for num in num_of_letters:
      letter =  chr(randint(ord('a'), ord('z')))
      name = name + letter
    add_people(id,name,age,sex)


def split_male_female(data:dict):
    """
    retrun two dictionaries one for male and one for female
    :param data:
    :return:
    """
    male={}
    female={}
    for id,detailes in data.items():
       if(detailes["sex"]=="male"):
           male[id]=detailes
       else:
           female[id] = detailes

    return male,female



def find_medien_avarage(dictionary: dict):
    """

    :param dictionary:
    :return:
    """
    sum=0
    lst=[]
    for value in dictionary.items():
        age=value[1]["age"]
        sum=sum+age
        lst.append(age)
    avarage=sum/len(dictionary.items())
    lst.sort()
    median=statistics.median(lst)
    print ("avarage=", avarage)
    print ("median=" , median)
    return avarage,median

def print_values_above(dictionary:dict,min_age :int=0):
    """

    :param dictionary:
    :param min_age:
    :return:
    """
    if min_age<0:
        raise  EOFError("min_age cant be smaller then 0")


    for item in dictionary.items():
        age =item[1]["age"]
        if(age>min_age):
            key=item[0]
            print(dictionary[key])

def main( numOfPeople:int=2, min_age:int=0, gender: str=""):
    """

    :param numOfPeople:
    :param min_age:
    :param gender:
    :return:
    """
    if(numOfPeople<1):
        raise EOFError("numOfPeople must be greater then 1")
    people_generator(numOfPeople)
    if gender=="male":
        male=split_male_female(data_set)[0]
        population = male
    elif gender=="female":
        female=split_male_female(data_set)[1]
        population = female
    elif gender=="":
        population=data_set
    else:
        raise EOFError("gender mast be male/female/empty")
    find_medien_avarage(population)
    print_values_above(population,min_age)
main(10,0,"female")