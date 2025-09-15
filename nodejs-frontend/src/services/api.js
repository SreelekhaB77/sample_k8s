import axios from "axios";

const API_BASE = "http://localhost:5000"; // Flask backend

export const getMessage = async () => {
  try {
    const response = await axios.get(`${API_BASE}/api/message`);
    return response.data.message;
  } catch (error) {
    console.error("Error fetching data:", error);
    return "Error connecting to Flask backend";
  }
};
