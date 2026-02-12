import { useEffect, useState} from 'react';
import api from "../services/api";

export default function Stats(){
    const [stats, setStats] = useState({});
    
    useEffect(() => {
        api.get("/stats").then(res=>setStats(res.data));
    }, []);

    return (
        <div>
            <h2>Totla Books: {stats.total_books}</h2>
            <h2>Average Rating: {stats.avg_rating}</h2>
            <h2>Median Pages: {stats.median_pages}</h2>
            <h2>Standard deviation: {stats.std_pages}</h2>
        </div>
    );
}