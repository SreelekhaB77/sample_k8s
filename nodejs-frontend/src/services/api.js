import axios from "axios";

const API_BASE = "/api"; // relative path, will be handled by NGINX

export const getMessage = async () => {
  try {
    const response = await axios.get(`${API_BASE}/api/message`);
    return response.data.message;
  } catch (error) {
    console.error("Error fetching data:", error);
    return "Error connecting to Flask backend";
  }
};
