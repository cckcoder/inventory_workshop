<template>
  <div class="container">
    <section class="section">
      <form @submit.prevent="handleSubmitForm">
        <div class="columns">
          <div class="column is-half is-offset-one-quarter">
            <h1 class="title">
              Create Inventory
              <span class="icon has-text-info ml-2">
                <i class="fa fa-cubes" aria-hidden="true"></i>
              </span>
            </h1>
            <div class="field">
              <label class="label" for="Name">Name: </label>
              <div class="control">
                <input v-model="inventory.name"
                  class="input" type="text" placeholder="Item name...">
              </div>
            </div>
            <div class="field">
              <label class="label" for="Name">Price: </label>
              <div class="control">
                <input v-model.number="inventory.price"
                  class="input" type="number" placeholder="Item Price...">
              </div>
            </div>
            <div class="field">
              <label class="label" for="Name">Stock Qty: </label>
              <div class="control">
                <input v-model.number="inventory.stock"
                  class="input" type="number" placeholder="Item Stock Qty...">
              </div>
            </div>
            <div class="file">
              <label class="file-label">
                <input @change="handleFileSelect"
                  class="file-input" type="file" name="resume">
                <span class="file-cta">
                  <span class="file-icon">
                    <i class="fa fa-upload"></i>
                  </span>
                  <span class="file-label">
                    Choose a file…
                  </span>
                </span>
              </label>
            </div>

            <div v-if="imageURL" class="section is-boxed">
              <img :src="imageURL" alt="" class="image">
            </div>

            <div class="columns mt-2">
              <div class="column">
                <div class="control">
                  <button class="button is-link mr-3">Submit</button>
                  <button class="button is-danger">Cancel</button>
                </div>
              </div>
            </div>
          </div>
        </div> <!-- end columns -->
      </form>
    </section>
  </div>
  {{ inventory }}
</template>

<script>
export default {
  data() {
    return {
      inventory: {
        name: '',
        price: '',
        stock: '',
        image_name: '',
        picture: '',
      },
      imageURL: ''
    }
  },
  methods: {
    handleFileSelect(event) {
      const reader = new FileReader();
      // For Preview
      reader.onload = event => {
        this.imageURL = event.target.result;
      };
      reader.readAsDataURL(event.target.files[0]);

      // For upload
      this.inventory.picture = event.target.files[0];
      this.inventory.image_name = event.target.files[0]['name']
    },
    handleSubmitForm() {
      let formData = new FormData()
      const { name, price, stock } = this.inventory
      formData.append("name", name)
      formData.append("price", price)
      formData.append("stock", stock)
      formData.append("image_name", this.inventory.image_name)
      formData.append("picture", this.inventory.picture)

      this.$store.dispatch('createInventory', formData)
    }
  }
}
</script>
