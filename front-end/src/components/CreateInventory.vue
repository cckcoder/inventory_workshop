<template>
    <div class="container">
        <div class="columns mx-2">
            <div class="column is-offset-4 is-4">
                <div class="forms">
                    <div class="field">
                        <label class="label">Name</label>
                        <div class="control">
                            <input v-model="inventory.name" class="input" type="text" placeholder="Text input">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Price</label>
                        <div class="control">
                            <input v-model="inventory.price" class="input" type="number" placeholder="Price">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Stock</label>
                        <div class="control">
                            <input v-model="inventory.stock" class="input" type="number" placeholder="Price">
                        </div>
                    </div>
                    <div class="file">
                    <label class="file-label">
                        <input class="file-input" type="file" @change="handleFileSelect">
                        <span class="file-cta">
                        <span class="file-icon">
                            <i class="fas fa-upload"></i>
                        </span>
                        <span class="file-label">
                            Choose a file…
                        </span>
                        </span>
                    </label>
                    <img v-if="imageURL" :src="imageURL" />
                    </div>
                </div>
            </div>
        </div>
    </div>
    {{ $data }}
</template>


<script>

export default {
    data() {
        return {
            inventory: {
                name: '',
                price: '',
                stock: '',
                image_name: ''
            },
            imageURL: null,
            image_file: null
        }
    },
    methods: {
        handleFileSelect(event) {
            const reader = new FileReader()
            reader.onload = event => {
                this.imageURL = event.target.result
            }
            reader.readAsDataURL(event.target.files[0])

            this.inventory.image_name = event.target.files[0]
        }

    }
}
</script>
