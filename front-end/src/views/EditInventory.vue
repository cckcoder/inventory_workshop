<template>
  <div class="container">
    <section class="section">
      <form @submit.prevent="handleSubmitForm">
        <div class="columns">
          <div class="column is-half is-offset-one-quarter">
            <h1 class="title">
              Edit Inventory
              <span class="icon has-text-info ml-2">
                <i class="fa fa-cubes" aria-hidden="true"></i>
              </span>
            </h1>
            <div class="field">
              <label class="label">Name: </label>
              <div class="control">
                <input v-model="itemInventory.name"
                  class="input" type="text" placeholder="Item name...">
              </div>
            </div>
            <div class="field">
              <label class="label">Price: </label>
              <div class="control">
                <input v-model.number="itemInventory.price"
                  class="input" type="number" placeholder="Item Price...">
              </div>
            </div>
            <div class="field">
              <label class="label">Stock Qty: </label>
              <div class="control">
                <input v-model.number="itemInventory.stock"
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

            <div v-if="itemImage" class="section is-boxed">
              <img :src="itemImage" alt="" class="image">
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
</template>

<script>
import { mapState } from 'vuex'

export default {
  props: ['id'],
  created() {
    this.$store.dispatch('fetchInventoryById', this.id)
  },
  data() {
    return {
      imageSize: 0,
      imagePreview: '',
    }
  },
  methods: {
    handleFileSelect(event) {
      const reader = new FileReader();
      // For Preview
      reader.onload = event => {
        this.imagePreview = event.target.result
      };
      reader.readAsDataURL(event.target.files[0])
      this.imageSize = event.target.files[0].size
      // For upload
      this.itemInventory.picture = event.target.files[0];
      this.itemInventory.image_name = event.target.files[0]['name']
    },
    handleSubmitForm() {
      let formData = new FormData()
      const { name, price, stock, picture, image_name } = this.itemInventory
      formData.append("name", name)
      formData.append("price", price)
      formData.append("stock", stock)
      formData.append("image_name", image_name)
      formData.append("picture", (! picture) ? 0 : picture)

      this.$store.dispatch('updateInventory', { id: this.id, formData: formData })
      this.$router.back()
    }

  },
  computed: {
    itemImage() {
      if (this.imageSize > 100) {
        return this.imagePreview
      } else {
        return `http://localhost:8001/static/images/${this.itemInventory.image_name}`
      }
    },
    ...mapState(['itemInventory'])
  }

}
</script>
