happy = ["good","happy","cheerful","contented","delighted","ecstatic","elated","glad","joyful","joyous","jubilant","lively","merry","overjoyed","peaceful","pleasant","pleased","thrilled",'upbeat','blessed','blest','blissful','blithe','cant complain','captivated','chipper','chirpy','content','convivial','exultant','flying high','gay','gleeful','gratified','intoxicated','jolly','laughing','light','looking good','mirthful','on cloud nine','peppy','perky','playful','sparkling','sunny','tickled','tickled pink','up','walking on air']
sad = ["worst","sad","bitterdismal","heartbroken","melancholy","mournful","pessimistic","somber","sorrowful","sorry","wistful","bereaved","blue","cheerless","dejected","despairing","despondent","disconsolate","distressed","doleful","down","down in dumps","down in mouth","downcast","forlorn","gloomy","glum","grief stricken","grieved","heartsick","heavyhearted","hurting","in doldrums","in grief","in the dumps","languishing","low","low spirited",'lugubrious','morbid','morose','out of sorts','pensive','sick at heart','troubled','weeping',"woebegone"]
dejected = ['worst',"dejected","downcast", "downhearted", "despondent", "disconsolate", "dispirited", "crestfallen", "cast down", "depressed", "disappointed", "disheartened", "discouraged", "demoralized", "crushed", "desolate", "heartbroken", "broken-hearted", "heavy hearted", "low-spirited"," in the doldrums", "sad", "unhappy", "doleful"," melancholy", "miserable", "woebegone", "forlorn", "long-faced","fed up", "wretched", "glum", "gloomy", "dismal", "shamefaced", "hangdog"]
angry = ['never','worst','angry','annoyed', 'bitter', 'enraged', 'exasperated', 'furious', 'heated', 'impassioned', 'indignant', 'irate', 'irritable', 'irritated', 'offended', 'outraged', 'resentful', 'sullen', 'uptight', 'affronted', 'antagonized', 'chafed', 'choleric', 'convulsed', 'cross', 'displeased', 'exacerbated', 'ferocious', 'fierce', 'fiery', 'fuming', 'galled', 'hateful', 'hot', 'huffy', 'ill-tempered', 'incensed', 'inflamed', 'infuriated', 'irascible', 'ireful', 'maddened', 'nettled', 'piqued', 'provoked', 'raging', 'riled', 'sore', 'splenetic', 'storming', 'sulky', 'tumultuous', 'turbulent']
depressed = ['depressed','despondent', 'morose', 'pessimistic', 'sad', 'unhappy', 'bleeding', 'blue', 'dejected', 'destroyed', 'dispirited', 'down', 'dragged', 'hurting', 'low', 'ripped', 'weeping', 'bad', 'bummed out', 'cast-down', 'crestfallen', 'crummy', 'disconsolate', 'down and out', 'down in the dumps', 'down in the mouth', 'downcast', 'downhearted', 'fed up', 'glum', 'grim', 'in a blue funk', 'in pain', 'in the dumps', 'in the pits', 'in the toilet', 'let down', 'low-down', 'low-spirited', 'lugubrious', 'melancholy', 'moody', 'on a downer', 'sob story', 'spiritless', 'taken down', 'torn up', 'woebegone']
question =['how','what','whom','where','when','how','who','why','whose','which']
threthen = ['kill','murder','rape', 'porn','stalking','killing', 'raping','menacing','assault','abduct','aducting','shoplifting', 'robbery']
bullying = [ 'fatso', 'nerd', 'ugly', 'slut', 'freak','jerk','nobody likes you','kill yourself','go die', 'i wish you die','bastard','fucker','fat','gay','annoying', 'racist', 'bitch', 'dead', 'noob', 'small', 'tiny', 'fake', 'loser', 'fuck', 'ugliest', 'dumb', 'stupid', 'losers', 'hell', 'surgery', 'trash', 'prick', 'ass', 'arse', 'cunt', 'shit', 'crap', 'dick', 'bloody', 'shag', 'stuff', 'screw']
romantic = ['sweet','beautiful','hot','lovesick','flirty','darling', 'admire', 'adorable', 'affection', 'love', 'angel', 'amazing', 'attraction', 'babe', 'baby', 'honey', 'cute', 'cuite', 'cutie', 'care', 'charming', 'cupid', 'elegant', 'girlfriend', 'boyfriend', 'valentine', 'gorgeous', 'cupcake', 'naughty', 'passion', 'queen', 'sassy', 'seductive', 'sweetheart', 'unqiue', 'warm']

main = str(input("Enter a sentance: "))

flag = 0

for element in happy:
        if element in main:
            print ("Happiness")
            flag = 1
            break

for element in sad:
        if element in main:
            print ("Sadness")
            flag = 2
            break
            
for element in dejected:
        if element in main:
            print ("Dejected")
            flag = 3
            break

for element in angry:
        if element in main:
            print ("Angry")
            flag = 4
            break
        
for element in depressed:
        if element in main:
            print ("depressed")
            flag = 5
            break

for element in question:
        if element in main:
            print ("Question")
            flag = 6
            break
        
for element in threthen:
        if element in main:
            print ("Thretening")
            flag = 7
            break

for element in bullying:
        if element in main:
            print ("Bullying")
            flag = 8
            break

if flag == 0:
    print("Can't detect try again")
