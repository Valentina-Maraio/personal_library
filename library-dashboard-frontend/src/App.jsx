import { useEffect, useState } from 'react';
import { getSummary, getBooksPerYears, getAuthors } from './api';

import {
  LineChart, Line,
  BarChart, Bar,
  XAxis, YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

export default function App() {

  const [summary, setSummary] = useState({});
  const [year, setYear] = useState([]);
  const [authors, setAuthors] = useState([]);

  useEffect(() => {
    getSummary().then(res => setSummary(res.data))
    getBooksPerYears().then(res => setYear(res.data))
    getAuthors().then(res => setAuthors(res.data))
  }, []);

  return (

    <>
      <div style={{ padding: 20 }}>
        <h1>Personal Library</h1>

        <h2>Total Books: {summary.total_books}</h2>
        <h2>Read Books: {summary.read_books}</h2>
        <h2>Avg Rating: {summary.avg_rating}</h2>
        <h2>Avg Pages: {summary.avg_pages}</h2>

        <h2>Books per Years</h2>

        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={year}>
            <XAxis dataKey="Year Published" />
            <YAxis />
            <Tooltip />
            <Line dataKey="count" />
          </LineChart>
        </ResponsiveContainer>

        <h2>top Authors</h2>

        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={authors}>
            <XAxis dataKey="author" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="count" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </>
  )
}