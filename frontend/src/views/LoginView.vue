<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">Log in</h1>
                <p class="mb-6 text-gray-500">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptates quis nihil obcaecati? Eum illum ullam maxime reiciendis esse eos unde facere, temporibus tempora voluptatibus neque laborum harum nisi non cumque.</p>
                <p class="font-bold">Don't have an account? <RouterLink to="/signup" class="underline">Click here</RouterLink> to create!</p>
            </div>
        </div>
        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6">
                    <div>
                        <label>Name</label><br>
                        <input type="text" placeholder="Your full name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>E-mail</label><br>
                        <input type="email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Password</label><br>
                        <input type="password" placeholder="Your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <div>
                        <label>Repeat password</label><br>
                        <input type="password" placeholder="Repeat your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                        <!-- <template v-if="errors.length > 0">
                            <div class="bg-red-300 text-white rounded-lg p-6">
                                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                            </div>
                        </template> -->

                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Log in</button>
                    </div>

                </form>
            </div>
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>

</style>