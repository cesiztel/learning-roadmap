import React from "react";
import Recipe from "./Recipe";

// refactor to -> function Menu({ title, recipes })
export default function Menu({ title, recipes }) {
  return (
    <article>
      <header>
        <h1>{title}</h1>
      </header>
      <div className="recipes">
        {recipes.map((recipe, i) => (
          <Recipe
            key={i}
            // can refactor to {...recipe}
            name={recipe.name}
            ingredients={recipe.ingredients}
            steps={recipe.steps}
          />
        ))}
      </div>
    </article>
  );
}
