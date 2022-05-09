import React, { useState } from "react";
import { FaStar } from "react-icons/fa";

const createArray = (length) => [...Array(length)];

export default function StarRating({ style = {}, total = 5, selected = 0 }) {
  const [selectedStars, setSelectedStars] = useState(selected);

  return (
    <div style={{ padding: "25px", ...style }}>
      {createArray(total).map((n, i) => (
        <Star
          key={i}
          selected={selectedStars > i}
          onSelect={() => setSelectedStars(i + 1)}
        />
      ))}
      <p>
        {selectedStars} of {total} stars
      </p>
    </div>
  );
}

const Star = ({ selected = false, onSelect = (f) => f }) => (
  <FaStar color={selected ? "red" : "grey"} onClick={onSelect} />
);
