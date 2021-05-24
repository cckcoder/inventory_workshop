<template>
 <div class="container mt-4">
        <div class="columns">
            <TheSideBar />
            <BoardInfo />
        </div>
    </div>
</template>

<script>
import TheSideBar from '@/components/core/TheSideBar'
import BoardInfo from '@/components/core/BoardInfo'

export default {
    components: {
        TheSideBar,
        BoardInfo
    }
}
</script>

<style>

</style>
