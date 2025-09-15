import React, { useEffect, useState } from "react";
import { getMessage } from "../services/api";

function Home() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    getMessage().then((res) => setMessage(res));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Flask API Response:</h2>
      <p>{message}</p>
    </div>
  );
}

export default Home;
