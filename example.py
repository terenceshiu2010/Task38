#************* HELP *****************
#REMEMBER THAT IF YOU NEED SUPPORT ON ANY ASPECT OF YOUR COURSE SIMPLY LOG IN TO www.hyperiondev.com/support TO:
#START A CHAT WITH YOUR MENTOR, SCHEDULE A CALL OR GET SUPPORT OVER EMAIL.
#*************************************

# *** NOTE ON COMMENTS ***
# This is a comment in Python.
# Comments can be placed anywhere in Python code and the computer ignores them - they are intended to be read by humans.
# Any line with a # in front of it is a comment and any with  ''' is also a docstring.
# Please read all the comments in this example file and all others.

import spacy  # importing spacy

en_core_web_sm = "C:/Users/User/AppData/Local/Programs/Python/Python311/Lib/" \
                 "site-packages/en_core_web_sm/en_core_web_sm-3.4.1"
nlp_sm = spacy.load(en_core_web_sm)

en_core_web_md = "C:/Users/User/AppData/Local/Programs/Python/Python311/Lib/" \
                 "site-packages/en_core_web_md/en_core_web_md-3.4.1"
nlp_md = spacy.load(en_core_web_md)

# Now we are going to look into longer texts and compare them. 
# Below we  have two lists: one containing complaints submitted to a company, and another of recipes found online.
# We want to establish how spaCy's model can identify similarities or dissimilarities between complaint and recipes. 

# Make sure to run this example file and read through the explanations.

# Below is a list of six complaints.
complaints = [ 'We bought a house in  CA. Our mortgage was handled by a company called ki. Soon after the mortgage was sold to ABC. Shortly after that XYZ took over the mortgage. The other day we got a notice not to send our payment to them but to loi instead. This is all so frustrating and wreaks of the  mortgage nightmare.',
'I got approved for a loan to buy a house I have submitted everything I need to for them I paid for the inspection and paid good faith check after all of that they said I did not get approved for the loan to cancel my contract because they do not want to wait for the down payments assistant said that the Sellers do not want to wait that long I feel like they are getting over on me I feel that they should have told me that I did not get approved before I spent my money and picked out a house Carrington mortgage in Ohio ',
'As per the correspondence, I received from : The University  This is to inform you that I have recently pulled my credit report and noticed that there is a collection listing from The University  on my credit report. I WAS never notified of this collection action or that I owed the debt. This letter is to inform you that I would like a verification of the debt and juilo ability to collect this money from me.',
'I am writing to dispute the follow information in my file.ON BOTH TransUnion & . for {$15000.00}. I have contacted this agency to advise to STOP CALLING ME this case was dismissed in court  2014. Please see the attached document from  County State Court. Thanking you in advanced regarding this matter.',
'I have not had a XXXX phone since early 2007. I have tried to resolve my bill in the past but it keeps reposting an old bill. I have no way to provide financial info from 8 years ago and they know that so they want me to prove it to them but I have no way to do that. Is there anyway to get  to find out how old it is.',
'I posted dated a check and mailed it for 2015 for my mortgage payment as my mortgage company will only take online payments if all the late charges are paid at once ( also illegal ), and the check was cashed on 2015 which cost me over {$70.00} in over draft fees with my bank.'
]

# We will now compare the similarity of the complaints to ascertain if spaCy's similarity
# model is able to distinguish between these long pieces of text.

print("-------------Complaints similarity with sm model---------------")
for token in complaints:
    token = nlp_sm(token)
    for token_ in complaints:
        token_ = nlp_sm(token_)
        print(token.similarity(token_))

print("-------------Complaints similarity with md model---------------")
for token in complaints:
    token = nlp_md(token)
    for token_ in complaints:
        token_ = nlp_md(token_)
        print(token.similarity(token_))

'''
-------------Complaints similarity with sm model---------------
1.0
C:\HyperionDev\Tasks\Task38\example.py:45: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(token.similarity(token_))
0.5090130466174222
0.7128344854285678
0.7586548283376252
0.5481749391003481
0.5452402796403908
0.5090130466174222
1.0
0.7270419360443711
0.44973754453402454
0.7358570174065904
0.539451287466797
0.7128344854285678
0.7270419360443711
1.0
0.7080282793889398
0.7212688611304713
0.6332525114389937
0.7586548283376252
0.44973754453402454
0.7080282793889398
1.0
0.5723389058792471
0.5394047113888343
0.5481749391003481
0.7358570174065904
0.7212688611304713
0.5723389058792471
1.0
0.49301711983715846
0.5452402796403908
0.539451287466797
0.6332525114389937
0.5394047113888343
0.49301711983715846
1.0
-------------Complaints similarity with md model---------------
1.0
0.835077095517691
0.9246800668484182
0.8959758607031337
0.8395325736974772
0.8622109066850939
0.835077095517691
1.0
0.8906698507861426
0.8145960252423514
0.9506983440908762
0.794650864741391
0.9246800668484182
0.8906698507861426
1.0
0.8905291077014569
0.88184629454754
0.8692563822438262
0.8959758607031337
0.8145960252423514
0.8905291077014569
1.0
0.8115091428079356
0.8775634120991097
0.8395325736974772
0.9506983440908762
0.88184629454754
0.8115091428079356
1.0
0.759590996735251
0.8622109066850939
0.794650864741391
0.8692563822438262
0.8775634120991097
0.759590996735251
1.0
'''


# Below is a list of six recipe instructions.

recipes= [ 'Bake in the preheated oven, stirring every 20 minutes, until sugar mixture has baked and caramelized onto popcorn and cashews, about 1 hour. Spread cashew caramel corn onto a parchment paper-lined baking sheet to cool. If desired, form into balls while still warm.',
'Combine brown sugar, corn syrup, butter, salt, and cream of tartar in a large saucepan. Bring to a boil, stirring constantly, until a candy thermometer inserted into the middle of the syrup, not touching the bottom, reads 260 degrees F (127 degrees C), 6 to 8 minutes.',
'Lift marshmallow fudge out of the pan by the edges of the foil and place on a large cutting board. Dip a large knife in the remaining confectioners\' sugar and slice fudge into 1 1/2-inch squares, continually dipping knife in the sugar after each slice.',
'Melt butter in a medium saucepan over medium heat; stir in condensed milk. Pour in chocolate chips; cook and stir until melted, 5 to 10 minutes.',
'Lightly grease a cookie sheet. Deflate the dough and turn it out onto a lightly floured surface. Roll the marzipan into a rope and place it in the center of the dough. Fold the dough over to cover it; pinch the seams together to seal. Place the loaf, seam side down, on the prepared baking sheet. Cover with a damp cloth and let rise until doubled in volume, about 40 minutes. Meanwhile, preheat oven to 350 degrees F (175 degrees C)',
'In a large bowl, cream together the butter, brown sugar, and white sugar. Beat in the instant pudding mix until blended. Stir in the eggs and vanilla. Blend in the flour mixture. Finally, stir in the chocolate chips and nuts. Drop cookies by rounded spoonfuls onto ungreased cookie sheets.'
]

# We will now compare the similarity of the recipes. to ascertain how well spaCy's similarity
# model is able to distinguish between them.

print("-------------Recipes similarity with sm model---------------")
for token in recipes:
    token = nlp_sm(token)
    for token_ in recipes:
        token_ = nlp_sm(token_)
        print(token.similarity(token_))

print("-------------Recipes similarity with md model---------------")
for token in recipes:
    token = nlp_md(token)
    for token_ in recipes:
        token_ = nlp_md(token_)
        print(token.similarity(token_))

'''
1.0
0.7084920860284759
0.6028835452295952
C:\HyperionDev\Tasks\Task38\example.py:156: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(token.similarity(token_))
0.7353469598150032
0.742543669049068
0.7203463346879786
0.7084920860284759
1.0
0.6627458558836178
0.6864292887388832
0.7183366047631227
0.7157533122977935
0.6028835452295952
0.6627458558836178
1.0
0.5845282964868923
0.6983784122312668
0.7327214060019888
0.7353469598150032
0.6864292887388832
0.5845282964868923
1.0
0.7533077379669134
0.7395232391726886
0.742543669049068
0.7183366047631227
0.6983784122312668
0.7533077379669134
1.0
0.8217725352900838
0.7203463346879786
0.7157533122977935
0.7327214060019888
0.7395232391726886
0.8217725352900838
1.0
-------------Recipes similarity with md model---------------
1.0
0.9058970680531702
0.876188281410988
0.8921914246767313
0.9362319998716938
0.9077991339554589
0.9058970680531702
1.0
0.8960303314307113
0.8683352787585712
0.9251986105731227
0.9092774425049626
0.876188281410988
0.8960303314307113
1.0
0.8206932481018961
0.9234997668651656
0.9066167238062411
0.8921914246767313
0.8683352787585712
0.8206932481018961
1.0
0.8436152755971948
0.8890459855149918
0.9362319998716938
0.9251986105731227
0.9234997668651656
0.8436152755971948
1.0
0.8970581769256016
0.9077991339554589
0.9092774425049626
0.9066167238062411
0.8890459855149918
0.8970581769256016
1.0
'''


# Now we want to obtain the extent of similarity between the complaints and the recipes.
# we will loop through every recipe instruction and compare it with a complaint.

print("-------------Recipes similarity with sm model---------------")

for token in recipes:
    token = nlp_sm(token)
    for token_ in complaints:
        token_ = nlp_sm(token_)
        print(token.similarity(token_))

print("-------------Recipes similarity with md model---------------")

for token in recipes:
    token = nlp_md(token)
    for token_ in complaints:
        token_ = nlp_md(token_)
        print(token.similarity(token_))

'''
0.5966323790672934
0.3016252128392763
C:\HyperionDev\Tasks\Task38\example.py:174: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(token.similarity(token_))
0.38263416407147594
0.5629846266692095
0.296555527068382
0.563792818513919
0.5024917576188229
0.1365427349914801
0.38694901428393064
0.5293672755251375
0.1609466229542559
0.5492883538552942
0.5717307684524712
0.23970944353302465
0.5015128759109356
0.5774550281213322
0.25644267374925117
0.47865004482282153
0.45971230146220154
0.13710956146501974
0.3076859397930708
0.5529147292867924
0.271413482850186
0.5467640587664471
0.6989333946320205
0.35674237652678187
0.5961972296632349
0.7574467156581833
0.5344295623356051
0.5674394925928256
0.6231520641071169
0.10303878804447938
0.4724182451659853
0.6803236382136475
0.30304246329307977
0.43135972184925
-------------Recipes similarity with md model---------------
0.7908974953781049
0.6548518295341987
0.739868093247277
0.7337805432695084
0.6703983067394562
0.7674085842432804
0.7580808759364783
0.5323926147261138
0.711456026675044
0.7008472217256502
0.5443126469769464
0.7254376905581942
0.7884092498717231
0.5253234387230952
0.7214799557383781
0.6939840662542774
0.5243623425430298
0.7301757749509531
0.6633546838990971
0.4596805288222233
0.5643795549917598
0.6354896663817883
0.4868229640175464
0.6469780047472005
0.8458760451310995
0.6612351139999046
0.7954999302389468
0.7757727786024005
0.6793217450290933
0.7921867919801224
0.7706409888372543
0.5407034497147122
0.6932683264149205
0.7135981756961652
0.5491464776242874
0.7118486371023985
'''

# What do you observe? Note that the similarity index has reduced from what we observed in the short-text example discussed in the content PDF.


# There are several ways to make your model more accurate with the similarity
# or even prediction such as feeding it with some training data. This could include
# more vocabulary about food and recipes if you are building a models concerning food.
# You can also head over to spaCy documentation here: https://spacy.io/usage/vectors-similarity
# and check out other cool stuff!
