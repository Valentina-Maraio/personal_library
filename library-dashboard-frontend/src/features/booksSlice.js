import {createSlice, createAsyncThunk} from '@reduxjs/toolkit';
import api from "../services/api";

export const fetchBooks = createAsyncThunk(

    "books/fetchBooks",
    async() => {
        const response = await api.get("/books");
        return response.data;
    }
);

export const addBooks = createAsyncThunk(

    "books/addBook",
    async(book) => {
        await api.post("/books", book);
        return book;
    }
);

const booksSlice = createSlice({
    name: "books",
    initialState: {
        books: [],
        status: "idle",
    },
    reducers: {},
    extraReducers: (builder) => {
        builder.addCase(fetchBooks.fulfilled, (state, action) => {
            state.books = action.payload;
        });
    },
});

export default booksSlice.reducer;