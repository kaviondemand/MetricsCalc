#CM to Inch Converter
def cm_to_inch():
 cm = float ( input ( "Centimeter(s): " ) )
 inches = cm / 2.54
 print ( " Inch(es): " , inches )

#Inch to CM Converter
def inch_to_cm():
 inches2 = float ( input ( " Inch(es): " ) )
 cm2 = inches2 * 2.54
 print ( " Centimeter(s) = " , cm2 )

#Kilogram to LBS Converter
def kg_to_lbs():
 kg = float ( input ( " Kilogram(s): " ) )
 lbs = kg * 2.204623
 print ( " LBS: " , lbs )


#LBS to Kilogram Converter
def lbs_to_kg():
 lbs2 = float ( input ( " LBS: " ) )
 kg2 = lbs2 / 2.204623
 print (  " Kilogram(s) " , kg2)


while True :
    print ( " \n ---  Converter ---" )
    print ( " 1. CM → Inches " )
    print ( " 2. Inches → CM" )
    print ( " 3. KG → LBS " )
    print ( " 4. LBS → KG " )
    print ( "5. Exit" )
    choice = input ( " Enter your choice (1-5):  " )
    if choice == ' 1 ' :
            cm_to_inch()
    elif choice == ' 2 ' :
            inch_to_cm()
    elif choice == ' 3 ' :
            kg_to_lbs()
    elif choice == ' 4 ' :
            lbs_to_kg()
    elif choice == ' 5 ' :
            print ( " Thanks for using Metrics Convertor! " )
            break
    else: 
        print ( " invalid choice select int 1-5  " )
