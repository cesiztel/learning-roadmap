import React from "react";

function Ingredient({ ingredient }) {
  return (
    <li>
      {ingredient.amount} {ingredient.measurement} of {ingredient.name}
    </li>
  );
}

export default function IngredientList({ list }) {
  return (
    <ul className="ingredients">
      {list.map((ingredient, i) => (
        <Ingredient key={i} ingredient={ingredient} />
      ))}
    </ul>
  );
}
