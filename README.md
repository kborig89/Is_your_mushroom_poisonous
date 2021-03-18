
# Machine Learning with Mushrooms
We have created a website to help identify if a mushroom is poisonous based on the description.

The web page uses a deep learning model to predict the poisonous nature of mushrooms based on user inputs in the format of a test.


Libraries used: Scikit-Learn, Pandas, HTML/CSS/Bootstrap, JS, Tableau, Flask
Host application using Heroku :  https://mushroomteam5.herokuapp.com/
Data : https://www.kaggle.com/uciml/mushroom-classification



# KEY
* Attribute Information: (classes: edible=e0 ,poisonous=p1)
* cap-shape: bell=b0,conical=c1,convex=x2,flat=f3, knobbed=k4,sunken=s5
* cap-surface: fibrous=f0,grooves=g1,scaly=y2,smooth=s3
* cap-color: brown=n0,buff=b1,cinnamon=c2,gray=g3,green=r4,pink=p5,purple=u6,red=e7,white=w8,yellow=y9
* odor:almond=a0,anise=l1,creosote=c2,fishy=y3,foul=f4,musty=m5,none=n6,pungent=p7,spicy=s8
* spore-print-color: black=k0,brown=n1,buff=b2,chocolate=h3,green=r4,orange=o5,purple=u6,white=w7,yellow=y8
* population: abundant=a0,clustered=c1,numerous=n2,scattered=s3,several=v4,solitary=y5


To run the site use the Heroku link above or use a development server by running the command python app.py in the terminal once naviagted to the cloned folder and copy the server link to a browser.   Navigate to the poisonous test on the left hand nav and input your mushroom characteristics.  The prediction will show below the submit button.
