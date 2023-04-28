import sqlite3

# Create table
try:
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        # cur.execute("INSERT INTO students (name, addr, city, zip) VALUES (?,?,?,?)", (nm, addr, city, zip))
        # cur.execute("drop TABLE REGISRATION")
        # cur.execute( "CREATE TABLE REGISTRATION (USERID INTEGER PRIMARY KEY AUTOINCREMENT, FULLNAME CHAR(100), EMAIL CHAR(200), PASSWORD CHAR(20),ROLE CHAR(20))")

       # cur.execute("INSERT INTO REGISTRATION (FULLNAME,EMAIL,PASSWORD,ROLE) VALUES(?,?,?,?)",                    ("Chiranjeevi", "chiru@proton.com", "123", ""))
       # con.commit()

        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('Lifespan','Lifespan Health Wellness','book.cat.healthWellness.html','Health Wellness','https://www.everythingzoomer.com/wp-content/uploads/2019/12/Lifespan.jpg','Ali Palmer','714')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('Breath','Breath Health Wellness','book.cat.healthWellness.html','Health Wellness','https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1656353759-413cAh3xCfL._SL500_.jpg?crop=1xw:1xh;center,top&resize=980:*','Yoselin Hanson','139')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('The sleep Revolution','The sleep Revolution Health Wellness','book.cat.healthWellness.html','Health Wellness','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEQjf-ETSuJhyVwQruMwuK2XwvK5G3CbthvA&usqp=CAU','Donald Koch','869')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('Women & The weight Loss','Women & The weight Loss Health Wellness','book.cat.healthWellness.html','Health Wellness','https://5.imimg.com/data5/RQ/XY/MY-10978766/women-500x500.png','Frances Powell','428')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('Books That Changed History','Books That Changed History History','book.cat.history.html','History','https://m.media-amazon.com/images/I/A14VAyvYsTL.jpg','Fiona Roy','406')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('The History of the Ancient World','The History of the Ancient World History','book.cat.history.html','History','https://assets.brightspot.abebooks.a2z.com/dims4/default/551cc46/2147483647/strip/true/crop/198x300+0+0/resize/198x300!/format/jpg/quality/90/?url=http%3A%2F%2Fabebooks-brightspot.s3.amazonaws.com%2F52%2F35%2Fe55c9a4a40319171e006198da2cf%2Fbest-history07.jpg','Hugh Santana','422')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('A Woman of No Importance','A Woman of No Importance History','book.cat.history.html','History','https://assets.brightspot.abebooks.a2z.com/dims4/default/48c8e78/2147483647/strip/true/crop/199x300+0+0/resize/398x600!/format/webp/quality/90/?url=http%3A%2F%2Fabebooks-brightspot.s3.amazonaws.com%2Ffc%2F11%2Fe640935b4a8285a850282ab8e846%2Fbest-history09.jpg','Julian Duarte','350')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('Democracy: A Life','Democracy: A Life History','book.cat.history.html','History','https://assets.brightspot.abebooks.a2z.com/dims4/default/fc17a0a/2147483647/strip/true/crop/200x300+0+0/resize/400x600!/format/webp/quality/90/?url=http%3A%2F%2Fabebooks-brightspot.s3.amazonaws.com%2F98%2F15%2Fc2b616ef4f8fa516774b5f7b5212%2Fbest-history10.jpg','Donte Quinn','132')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('Grant','Grant History','book.cat.history.html','History','https://assets.brightspot.abebooks.a2z.com/dims4/default/08f3d78/2147483647/strip/true/crop/195x300+0+0/resize/390x600!/format/webp/quality/90/?url=http%3A%2F%2Fabebooks-brightspot.s3.amazonaws.com%2F9a%2Fef%2Fd4bf8b1a40d180e2e93fddc869bb%2Fbest-history01.jpg','Gabrielle Shea','407')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('Rich Dad Poor Dad','Rich Dad Poor Dad Personal Growth','book.cat.personGrowth.html','Personal Growth','https://www.99booksstore.com/uploaded_files/product/284481191.webp','Danika Brewer','411')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('The Growth Mindset','The Growth Mindset Personal Growth','book.cat.personGrowth.html','Personal Growth','https://m.media-amazon.com/images/I/51BGQYwxB9L.jpg','Jovanni Moran','713')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('Best Self','Best Self Personal Growth','book.cat.personGrowth.html','Personal Growth','https://fourminutebooks.com/wp-content/uploads/2020/11/self-help-books-6.jpg','Darian Davenport','435')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('Think and Grow Rich','Think and Grow Rich Personal Growth','book.cat.personGrowth.html','Personal Growth','https://quickbooost.com/wp-content/uploads/2020/07/Think-Grow-Rich.jpg','Stella Wall','909')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('Failing Forward','Failing Forward Personal Growth','book.cat.personGrowth.html','Personal Growth','https://cdn.lifehack.org/wp-content/uploads/2022/11/41gHYiOWQ6L._SL500_.webp','Zander Bishop','129')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('A Desolation Called Peace','A Desolation Called Peace Science Fiction','book.cat.scifi.html','Science Fiction','https://marketing.prowritingaid.com/a-desolation-called-peace-book.jpg','Vance Waller','639')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('The Kaiju Preservation Society','The Kaiju Preservation Society Science Fiction','book.cat.scifi.html','Science Fiction','https://ik.imagekit.io/panmac/tr:f-auto,di-placeholder_portrait_aMjPtD9YZ.jpg,w-171/edition/9781509835317.jpg','Catherine Hammond','243')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('The Hunder Games','The Hunder Games Science Fiction','book.cat.scifi.html','Science Fiction','https://cdn.vox-cdn.com/thumbor/9B13TohweY2rMunkLbaxPp33oQ8=/0x0:792x1200/1200x0/filters:focal(0x0:792x1200):no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/21960146/61JfGcL2ljL.jpg','Tanner Barber','183')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('Catching Fire','Catching Fire Science Fiction','book.cat.scifi.html','Science Fiction','https://s2982.pcdn.co/wp-content/uploads/2019/04/catching-fire-199x300.jpg.optimal.jpg','Marcus Jennings','569')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('The Last Astronaut','The Last Astronaut Science Fiction','book.cat.scifi.html','Science Fiction','https://fivebooks.com/app/uploads/books/BC_0316419575-194x300.jpg','Camden Casey','559')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('Land of Second Chances','Land of Second Chances Sports','book.cat.sports.html','Sports','https://hips.hearstapps.com/hmg-prod/images/tim-lewis-land-of-second-chances-1641916813.jpeg?resize=640:*','Regina Daniels','499')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('Football Against The Enemy by Simon Kuper','Football Against The Enemy by Simon Kuper Sports','book.cat.sports.html','Sports','https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1587460131-619J1X8tZL.jpg?crop=1xw:1xh;center,top&resize=980:*','Leonel Shaw','117')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('Addicted by Tony Adams','Addicted by Tony Adams Sports','book.cat.sports.html','Sports','https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1587460434-41S4NYE311L._SL500_.jpg?crop=1xw:1xh;center,top&resize=980:*','Alice Weber','914')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('I Think Therefore I Play','I Think Therefore I Play Sports','book.cat.sports.html','Sports','https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1587460482-51bPpEyEvL.jpg?crop=1xw:1xh;center,top&resize=980:*','Luz Buchanan','511')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('The Damned Utd','The Damned Utd Sports','book.cat.sports.html','Sports','https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1587460520-51jELd7OWTL.jpg?crop=1xw:1xh;center,top&resize=980:*','Gavyn Marshall','899')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('The Travel Book','The Travel Book Travel','book.cat.travel.html','Travel','https://m.media-amazon.com/images/I/81jkS9zRZ4L.jpg','Madisyn Vasquez','404')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('Travel','Travel Travel','book.cat.travel.html','Travel','https://m.media-amazon.com/images/I/415qF9qEF2L.jpg','Isabella Sharp','581')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('Lands of Lost Borders','Lands of Lost Borders Travel','book.cat.travel.html','Travel','https://imageio.forbes.com/blogs-images/jonisweet/files/2018/08/Lands-of-Lost-Borders-FORBES.jpg?height=400&width=640&fit=bounds','Kamari Golden','583')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('The Meaning of Travel','The Meaning of Travel Travel','book.cat.travel.html','Travel','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMA1tPb2neXa7k_3RYnhbtqBtoUEE5OCBxog&usqp=CAU','Margaret Mercado','446')")
        cur.execute("INSERT INTO BOOKS (BOOKNAME, SEARCHSTRING, LINK, CATEGORY, IMGLINK, AUTHOR, PRICE) VALUES ('Blue Highways','Blue Highways Travel','book.cat.travel.html','Travel','https://imageio.forbes.com/blogs-images/jonisweet/files/2018/08/Blue-Highways-FORBES.jpg?height=400&width=640&fit=bounds','Urijah Curry','744')")

        # cur.execute(
        #     "CREATE TABLE CONTACTQUERIES (QID INTEGER PRIMARY KEY AUTOINCREMENT, NAME CHAR(500), EMAIL CHAR(50), QUERY CHAR(500) )")

        rows = cur.fetchall()
        print(rows)
        # cur.close()

        msg = "Query Executed Successfully"
except Exception as e:
    con.rollback()
    msg = "Error in executing Query"
    print(e)

print(msg)
