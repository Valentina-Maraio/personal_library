import {configureStore} from '@reduxjs/toolkit';
import bookReducer from '../features/booksSlice';

export const store = configureStore({

    reducer: {
        books: bookReducer,
    },

});