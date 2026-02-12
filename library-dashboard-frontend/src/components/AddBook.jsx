import { useDispatch} from 'react-redux';
import {addBook} from "../features/booksSlice";

export default function AddBook(){
    const dispatch = useDispatch();
    const handleSubmit = (e) => {
        e.preventDefault();

        const form = e.target;
        dispatch(addBook({
            title: form.title.value,
            author: form.author.value,
            year: parseInt(form.year.value),
            pages: parseInt(form.pages.value),
            rating: parseInt(form.rating.value),
            shelf: form.shelf.value,
        }));
    };

    return (

        <form onSubmit={handleSubmit}>
            <input name="title" placeholder="Title" />
            <input name="author" placeholder="Author" />
            <input name="year" placeholder="Year" />
            <input name="pages" placeholder="Pages" />
            <input name="rating" placeholder="Rating" />
            <input name="shelf" placeholder="Shelf" />
            
            <button>Add Book</button>
        </form>
    );
}