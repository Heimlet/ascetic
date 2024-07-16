import { createStore } from 'vuex';
import { cart } from './modules/cart.js';

const store = createStore({
    modules: {
        cart,
    }
});

export default store;