import axios from "axios";

const API = "http://127.0.0.1:8000";

export const getSummary = () => axios.get(`${API}/summary`);
export const getBooksPerYears = () => axios.get(`${API}/books_per_year`);
export const getAuthors = () => axios.get(`${API}/top_authors`);