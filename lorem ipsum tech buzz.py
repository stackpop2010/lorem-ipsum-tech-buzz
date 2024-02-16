import random

latin_list = ["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing","elit","sed", "do", "eius","modi", "tempor", "incididunt", "ut",
              "labore", "et", "dolore", "magna","aliqua", "enim", "ad", "minim", "veniam", "quis", "nostrumd", "exercitation",
              "ullam", "co", "pariatur", "exceptur", "sint", "obcaecati", "cupidtat", "non", "pro", "ident", "sunt",
              "culpa","qui", "officia", "deserunt", "mollit", "anim", "id", "est", "laboru", "et", "harum", "de", "re", "ud", "facilis", "est", "er",
              "expedi", "disi", "nam", "liber", "tempor", "cum", "soluta", "nobis", "elige", "quod", "maxim", "placeat", "facer",
              "possim", "omins", "volupt", "assumenda", "est", "omnis", "dolor", "repellenda"]

tech_list = ["Datafication","Net Neutrality","Non-Fungible Tokens","Metaverse","Digital Divide","Everything As A Service",
"Hyper-Personalization","Gamification","Wantrepreneur", "SQL", "C#", "Front End", "Full Stack", "Web Dev",
"Augmented Reality","Virtual reality","Robotics","Smart Industry 4.0","Robotic Process Automation","Neural Networks",
"Blockchain","Technological Unemployment","Computer Vision", "Cyber Crime", "Security", "Hackathon",
"Distributed Cloud","Artificial Intelligence","Large Language Models","Hyperautomation","Chat GPT","Quantum Computing","5G Connectivity",
"FAANG","Web3","Multiexperience","Google","Cloud-Native Platforms","Big Data","Social Media","Platform as a Service",
"Chatbots","Cloud Computing","Cryptocurrency","Data Mining","scams","Python","Digitization","Digital Transformation",
"Digital Disruption","Agile","Internet of Things","Machine Learning","RAM","Actionable Analytics","Microservices",
"User Experience","Infrastructure as a Service"]

def gibberish():
    len=input("Pick a number between 1 and 100: ")

    if int(len) < 0 or int(len)> 100:
        print("try again, invalid input")
        return gibberish()

    #makes your string 70% latin and 30% buzz words
    k = float(len)*0.7
    j = float(len)*0.3

    #creates and concatinates latin and buzz words
    new_list =list(random.choices(latin_list, k=int(k)))+(random.choices(tech_list, k=int(j)))
    #shuffles the order
    random.shuffle(new_list)
    #converts to string
    print_string = ""
    for word in new_list:
        print_string += " " + word

    return print_string



print(gibberish())

