<script setup>

import NavBar from "@/components/navbar/NavBar.vue";
import api from "@/js/http/api.js";
import {useUserStore} from "@/stores/user.js";
import {onMounted} from "vue";
import {useRoute, useRouter} from "vue-router";

const user = useUserStore()
const route =  useRoute()
const router = useRouter()

onMounted(async () => {
  try {
    const res = await api.get('/api/user/account/get_user_info/')
    const data = res.data
    if(data.result === "success") {
      user.setUserInfo(data)
    }
  } catch (err) {

  } finally {
    user.setPulledUserInfo(true)

    if(route.meta.needLogin && !user.isLogin()) {
      await router.replace({
        name: 'login-account-login-index',
      })
    }
  }
})
</script>


<template>
  <NavBar>
    <RouterView></RouterView>
  </NavBar>

</template>

<style scoped>

</style>
