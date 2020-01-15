const luke = { 
	name: "Luke Skywalker", 
	type: "Jedi", 
	appearsIn: ["NEWHOPE", "EMPIRE", "JEDI"], 
	hero: true,
	age: 28
};

const han = { 
	name: "Han Solo", 
	type: "Human", 
	appearsIn: ["NEWHOPE", "JEDI"], 
	hero: true,
	age: 35
};

const r2 = { 
	name: "R2-D2", 
	type: "Droid", 
	appearsIn: ["NEWHOPE", "EMPIRE", "JEDI"], 
	hero: true,
	skills: ["protocol"]
};

const cpo = { 
	name: "C-3PO", 
	type: "Droid", 
	appearsIn: ["NEWHOPE", "EMPIRE", "JEDI"], 
	hero: true,
	skills: ["open dors", "pilor starships"] 
};

const vader = { name: "Darth Vader", type: "Sith", appearsIn: ["NEWHOPE", "EMPIRE", "JEDI"], hero: false };

exports.buildUniverse = function () {
	luke.father = [vader];
	luke.friends = [han, r2, cpo];
	han.friends = [luke, r2, cpo];
	r2.friends = [han, luke, cpo];
	cpo.friends = [han, luke, r2];
	vader.friends = [];

	return [han, luke, r2, cpo, vader];
}
