<template>
    <div class="has-text-center">
        <figure class="image is-64x64 is-inline-block">
            <img :src="getImage">
        </figure>
    </div>
</template>

<script>
export default {
  name: 'ImageBase',
  props: {
    image_name: String,
  },
    computed: {
        getImage() {
            return `http://localhost:8001/static/images/${this.image_name}`
        }
    }
}
</script>

<style scoped>
img {
  width: 80%;
}
</style>
