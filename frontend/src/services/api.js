import axiosInstance from '@/axios.js';

export const fetchProducts = async (page = null, perPage = null, category = null, is_trending=null, is_proud=null) => {
    try {
        const params = {};
        if (page !== null && perPage !== null) {
            params.page = page;
            params.page_size = perPage;
        }
        if (category && category !== 'all') {
            params.category = category;
        }
        params.is_trending_now = is_trending ? 1 : undefined;
        params.is_proud_of = is_proud ? 1 : undefined;
        const response = await axiosInstance.get('/api/v1/products/', { params });
        return {
            products: response.data.results || response.data,
            total: response.data.count || response.data.length
        };
    } catch (error) {
        console.error('Failed to fetch products:', error);
        throw error;
    }
};

export const fetchProductById = async (id) => {
    try {
        const response = await axiosInstance.get(`/api/v1/products/${id}/`);
        return response.data;
    } catch (error) {
        console.error('Failed to fetch product by ID:', error);
        throw error;
    }
};

export const fetchCategories = async (is_main_page=null) => {
    try {
        const params = {};
        params.is_main_page = is_main_page ? 1 : undefined;

        const response = await axiosInstance.get('/api/v1/categories/', { params });
        return response.data;
    } catch (error) {
        console.error('Failed to fetch categories:', error);
        throw error;
    }
};
