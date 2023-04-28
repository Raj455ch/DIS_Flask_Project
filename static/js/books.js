const booksData = [
	{
		bookName: "Health &amp; Wellness",
		searchString: "Health &amp; Wellness Health Wellness",
		link: "book.cat.healthWellness.html",
		category: "Health Wellness",
		imgLink: "https://m.media-amazon.com/images/I/81xtQ1l2IGL.jpg",
	},
	{
		bookName: "Lifespan",
		searchString: "Lifespan Health Wellness",
		link: "book.cat.healthWellness.html",
		category: "Health Wellness",
		imgLink: "https://www.everythingzoomer.com/wp-content/uploads/2019/12/Lifespan.jpg",
	},
	{
		bookName: "Breath",
		searchString: "Breath Health Wellness",
		link: "book.cat.healthWellness.html",
		category: "Health Wellness",
		imgLink: "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1656353759-413cAh3xCfL._SL500_.jpg?crop=1xw:1xh;center,top&amp;resize=980:*",
	},
	{
		bookName: "The sleep Revolution",
		searchString: "The sleep Revolution Health Wellness",
		link: "book.cat.healthWellness.html",
		category: "Health Wellness",
		imgLink: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEQjf-ETSuJhyVwQruMwuK2XwvK5G3CbthvA&amp;usqp=CAU",
	},
	{
		bookName: "Women &amp; The weight Loss",
		searchString: "Women &amp; The weight Loss Health Wellness",
		link: "book.cat.healthWellness.html",
		category: "Health Wellness",
		imgLink: "https://5.imimg.com/data5/RQ/XY/MY-10978766/women-500x500.png",
	},
	{
		bookName: "Books That Changed History",
		searchString: "Books That Changed History History",
		link: "book.cat.history.html",
		category: "History",
		imgLink: "https://m.media-amazon.com/images/I/A14VAyvYsTL.jpg",
	},
	{
		bookName: "The History of the Ancient World",
		searchString: "The History of the Ancient World History",
		link: "book.cat.history.html",
		category: "History",
		imgLink: "https://assets.brightspot.abebooks.a2z.com/dims4/default/551cc46/2147483647/strip/true/crop/198x300+0+0/resize/198x300!/format/jpg/quality/90/?url=http%3A%2F%2Fabebooks-brightspot.s3.amazonaws.com%2F52%2F35%2Fe55c9a4a40319171e006198da2cf%2Fbest-history07.jpg",
	},
	{
		bookName: "A Woman of No Importance",
		searchString: "A Woman of No Importance History",
		link: "book.cat.history.html",
		category: "History",
		imgLink: "https://assets.brightspot.abebooks.a2z.com/dims4/default/48c8e78/2147483647/strip/true/crop/199x300+0+0/resize/398x600!/format/webp/quality/90/?url=http%3A%2F%2Fabebooks-brightspot.s3.amazonaws.com%2Ffc%2F11%2Fe640935b4a8285a850282ab8e846%2Fbest-history09.jpg",
	},
	{
		bookName: "Democracy: A Life",
		searchString: "Democracy: A Life History",
		link: "book.cat.history.html",
		category: "History",
		imgLink: "https://assets.brightspot.abebooks.a2z.com/dims4/default/fc17a0a/2147483647/strip/true/crop/200x300+0+0/resize/400x600!/format/webp/quality/90/?url=http%3A%2F%2Fabebooks-brightspot.s3.amazonaws.com%2F98%2F15%2Fc2b616ef4f8fa516774b5f7b5212%2Fbest-history10.jpg",
	},
	{
		bookName: "Grant",
		searchString: "Grant History",
		link: "book.cat.history.html",
		category: "History",
		imgLink: "https://assets.brightspot.abebooks.a2z.com/dims4/default/08f3d78/2147483647/strip/true/crop/195x300+0+0/resize/390x600!/format/webp/quality/90/?url=http%3A%2F%2Fabebooks-brightspot.s3.amazonaws.com%2F9a%2Fef%2Fd4bf8b1a40d180e2e93fddc869bb%2Fbest-history01.jpg",
	},
	{
		bookName: "Rich Dad Poor Dad",
		searchString: "Rich Dad Poor Dad Personal Growth",
		link: "book.cat.personGrowth.html",
		category: "Personal Growth",
		imgLink: "https://www.99booksstore.com/uploaded_files/product/284481191.webp",
	},
	{
		bookName: "The Growth Mindset",
		searchString: "The Growth Mindset Personal Growth",
		link: "book.cat.personGrowth.html",
		category: "Personal Growth",
		imgLink: "https://m.media-amazon.com/images/I/51BGQYwxB9L.jpg",
	},
	{
		bookName: "Best Self",
		searchString: "Best Self Personal Growth",
		link: "book.cat.personGrowth.html",
		category: "Personal Growth",
		imgLink: "https://fourminutebooks.com/wp-content/uploads/2020/11/self-help-books-6.jpg",
	},
	{
		bookName: "Think and Grow Rich",
		searchString: "Think and Grow Rich Personal Growth",
		link: "book.cat.personGrowth.html",
		category: "Personal Growth",
		imgLink: "https://quickbooost.com/wp-content/uploads/2020/07/Think-Grow-Rich.jpg",
	},
	{
		bookName: "Failing Forward",
		searchString: "Failing Forward Personal Growth",
		link: "book.cat.personGrowth.html",
		category: "Personal Growth",
		imgLink: "https://cdn.lifehack.org/wp-content/uploads/2022/11/41gHYiOWQ6L._SL500_.webp",
	},
	{
		bookName: "A Desolation Called Peace",
		searchString: "A Desolation Called Peace Science Fiction",
		link: "book.cat.scifi.html",
		category: "Science Fiction",
		imgLink: "https://marketing.prowritingaid.com/a-desolation-called-peace-book.jpg",
	},
	{
		bookName: "The Kaiju Preservation Society",
		searchString: "The Kaiju Preservation Society Science Fiction",
		link: "book.cat.scifi.html",
		category: "Science Fiction",
		imgLink: "https://ik.imagekit.io/panmac/tr:f-auto,di-placeholder_portrait_aMjPtD9YZ.jpg,w-171/edition/9781509835317.jpg",
	},
	{
		bookName: "The Hunder Games",
		searchString: "The Hunder Games Science Fiction",
		link: "book.cat.scifi.html",
		category: "Science Fiction",
		imgLink: "https://cdn.vox-cdn.com/thumbor/9B13TohweY2rMunkLbaxPp33oQ8=/0x0:792x1200/1200x0/filters:focal(0x0:792x1200):no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/21960146/61JfGcL2ljL.jpg",
	},
	{
		bookName: "Catching Fire",
		searchString: "Catching Fire Science Fiction",
		link: "book.cat.scifi.html",
		category: "Science Fiction",
		imgLink: "https://s2982.pcdn.co/wp-content/uploads/2019/04/catching-fire-199x300.jpg.optimal.jpg",
	},
	{
		bookName: "The Last Astronaut",
		searchString: "The Last Astronaut Science Fiction",
		link: "book.cat.scifi.html",
		category: "Science Fiction",
		imgLink: "https://fivebooks.com/app/uploads/books/BC_0316419575-194x300.jpg",
	},
	{
		bookName: "Land of Second Chances",
		searchString: "Land of Second Chances Sports",
		link: "book.cat.sports.html",
		category: "Sports",
		imgLink: "https://hips.hearstapps.com/hmg-prod/images/tim-lewis-land-of-second-chances-1641916813.jpeg?resize=640:*",
	},
	{
		bookName: "Football Against The Enemy by Simon Kuper",
		searchString: "Football Against The Enemy by Simon Kuper Sports",
		link: "book.cat.sports.html",
		category: "Sports",
		imgLink: "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1587460131-619J1X8tZL.jpg?crop=1xw:1xh;center,top&amp;resize=980:*",
	},
	{
		bookName: "Addicted by Tony Adams",
		searchString: "Addicted by Tony Adams Sports",
		link: "book.cat.sports.html",
		category: "Sports",
		imgLink: "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1587460434-41S4NYE311L._SL500_.jpg?crop=1xw:1xh;center,top&amp;resize=980:*",
	},
	{
		bookName: "I Think Therefore I Play",
		searchString: "I Think Therefore I Play Sports",
		link: "book.cat.sports.html",
		category: "Sports",
		imgLink: "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1587460482-51bPpEyEvL.jpg?crop=1xw:1xh;center,top&amp;resize=980:*",
	},
	{
		bookName: "The Damned Utd",
		searchString: "The Damned Utd Sports",
		link: "book.cat.sports.html",
		category: "Sports",
		imgLink: "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1587460520-51jELd7OWTL.jpg?crop=1xw:1xh;center,top&amp;resize=980:*",
	},
	{
		bookName: "The Travel Book",
		searchString: "The Travel Book Travel",
		link: "book.cat.travel.html",
		category: "Travel",
		imgLink: "https://m.media-amazon.com/images/I/81jkS9zRZ4L.jpg",
	},
	{
		bookName: "Travel",
		searchString: "Travel Travel",
		link: "book.cat.travel.html",
		category: "Travel",
		imgLink: "https://m.media-amazon.com/images/I/415qF9qEF2L.jpg",
	},
	{
		bookName: "Lands of Lost Borders",
		searchString: "Lands of Lost Borders Travel",
		link: "book.cat.travel.html",
		category: "Travel",
		imgLink: "https://imageio.forbes.com/blogs-images/jonisweet/files/2018/08/Lands-of-Lost-Borders-FORBES.jpg?height=400&amp;width=640&amp;fit=bounds",
	},
	{
		bookName: "The Meaning of Travel",
		searchString: "The Meaning of Travel Travel",
		link: "book.cat.travel.html",
		category: "Travel",
		imgLink: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMA1tPb2neXa7k_3RYnhbtqBtoUEE5OCBxog&amp;usqp=CAU",
	},
	{
		bookName: "Blue Highways",
		searchString: "Blue Highways Travel",
		link: "book.cat.travel.html",
		category: "Travel",
		imgLink: "https://imageio.forbes.com/blogs-images/jonisweet/files/2018/08/Blue-Highways-FORBES.jpg?height=400&amp;width=640&amp;fit=bounds",
	},
];
export { booksData };