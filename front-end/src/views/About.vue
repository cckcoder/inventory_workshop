<template>
  <div class="card">
    <div class="card-image">
      <figure class="image is-4">
        <img src="@/assets/stackpython.png" alt="Placeholder image">
      </figure>
    </div>
    <div class="card-content">
      <div class="media">
        <div class="media-left">
          <figure class="image is-64x64 is-square">
            <img class="is-rounded"
              src="@/assets/stackpython.png" alt="Placeholder image">
          </figure>
        </div>
        <div class="media-content">
          <p class="title is-4">VueJs and FastAPI</p>
          <p class="subtitle is-6">@Stackpython</p>
        </div>
      </div>

      <div class="content">
        สวัสดีพวกเราชาว Stackpython
        เราคือทีมงานคุณภาพ เกี่ยวกับการพัฒนาทักษะ ทาง Programming และ Web Development
        และ แชร์ ความรู้เกี่ยวกับทางด้าน เทคโนโลยี เพื่อเป็นประโยชน์แก่ ผู้ที่สนใจ ไม่ว่าจะเป็นในส่วนของ
        Blog, Medium และ Youtube
      </div>
    </div>
    <footer class="card-footer py-3">
      <div class="ml-3">
        <time :datetime="getTimeNow">{{ getTimeNow }}</time>
      </div>
    </footer>
  </div>
</template>

<script>

export default {
  name: 'About',
  computed: {
    getTimeNow() {
      let today = new Date()
      let options = {
          month: 'long',
          year: 'numeric'
        }
      let time = today.toLocaleTimeString('default', options)
      return `${time}`
    }
  }
}
</script>
