export const cart = {
    namespaced: true,
    state: () => ({
        cartItems: [],
    }),
    mutations: {
        addItemToCart(state, item) {
            state.cartItems.push(item);
        },
        removeItemFromCart(state, itemId) {
            state.cartItems = state.cartItems.filter(item => item.id !== itemId);
        },
        clearCart(state) {
            state.cartItems = [];
        },
        increaseQuantity(state, itemId) {
            const item = state.cartItems.find(item => item.id === itemId);
            if (item) {
                state.cartItems.push(item);
            }
        },
        decreaseQuantity(state, itemId) {
            const itemIndex = state.cartItems.findIndex(item => item.id === itemId);
            if (itemIndex !== -1) {
                state.cartItems.splice(itemIndex, 1);
            }
        }
    },
    actions: {
        addItemToCart({ commit }, item) {
            commit('addItemToCart', item);
        },
        removeItemFromCart({ commit }, itemId) {
            commit('removeItemFromCart', itemId);
        },
        clearCart({ commit }) {
            commit('clearCart');
        },
        increaseQuantity({ commit }, itemId) {
            commit('increaseQuantity', itemId);
        },
        decreaseQuantity({ commit }, itemId) {
            commit('decreaseQuantity', itemId);
        }
    },
    getters: {
        cartItems: state => {
            const groupedItems = state.cartItems.reduce((acc, item) => {
                if (!acc[item.id]) {
                    acc[item.id] = { ...item, count: 0, totalPrice: 0 };
                }
                acc[item.id].count += 1;
                acc[item.id].totalPrice += +item.price;
                return acc;
            }, {});

            return Object.values(groupedItems).map(({ id, count, totalPrice, ...details }) => ({
                id,
                count,
                totalPrice,
                details,
            }));
        },
        cartItemCount: state => state.cartItems.length,
        subtotal: (state, getters) => getters.cartItems.reduce((acc, item) => acc + item.totalPrice, 0)
    }
};
