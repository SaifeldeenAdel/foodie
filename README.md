# **FOODIE**
<br>

# **Description**

**FOODIE** is a web application used for searching for and saving your favourite recipes. Instead of searching for recipes all over the place on all of the different cooking/recipe websites, FOODIE brings it all together so that you can reach all of these websites using only one search bar. 

On top of that, users can save the recipes they like all in one place instead of having the recipes saved on all the different websites that they come from.

It is built primarily using **python/flask, html, css and SQL**. 


<br>
<br>

# **Key Features**
* **User login system**. Opens the opportunity for a "My recipes" page
    * ### Users can also change passwords
* **Search for Recipes** page where you can...search for recipes. (with the help of the EDAMAM Recipe search API, more on that later)
* **My Recipes** page where each user can access the recipes they saved. 
* **Expanded page** for each recipe where a little more info is given about the recipe and from there, a user can add it to their recipes and/or visit the actual website it's from.

<br>
<br>

# **Walkthrough**
1. Registering as a user.
2. Logging in (log in is required to access the other pages)
3. Search for a recipe. 
4. Expand it if you like it, from here you can either check out the full recipe on its original website that it came from or you can click on the Add to my Recipes button.
5. After clicking Add, you're redirected to your "My recipes" page where you'll see that it's been added. 
6. You can then expand it again and this time click on the Remove from My Recipes button and it'll be removed.
6. Now go search and add as many recipes as you like! 

<br>

# **In-depth**
## **Taking a closer look at the code:**

**Implementation Details:** This webapp has implementations of 
* **Flask WTForms:** makes it much easier for incorporating all kinds of validators 
* **SQLAlchemy**
* Style-wise: several elements from **Bootstrap** have been used.

<br>

**About API:** All of the data related to the recipes is retrieved with the help of the [EDAMAM Recipe Search API](https://developer.edamam.com/edamam-docs-recipe-api). When it's queried by the user's search, a json type object is retrieved which I then loop over in jinja to display all the recipes that came out of the search.

<br>

**SQL:** When a user clicks to add or remove a recipe, an SQL query runs which adds or pops a row from a Recipes table which has a many-to-one relationship with the Users table as to know which user to add to/remove from.

<br>
<br>

# Credit
### Sources that helped me the most along this journey:
* [CS50 Discord](https://discord.com/invite/cs50)
* [CSS Basics](https://www.w3schools.com/css/css_intro.asp)
* [Working with JSON data](https://www.youtube.com/watch?v=9N6a-VLBa2I)
* [Getting started with SQLAlchemy](https://www.youtube.com/watch?v=jTiyt6W1Qpo)
* [Custom jinja filter for encoding URLs](https://stackoverflow.com/questions/33450404/quote-plus-url-encode-filter-in-jinja2)




