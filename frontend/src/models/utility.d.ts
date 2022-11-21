declare type Nullable<T> = T | null
declare type Nillable<T> = T | null | undefined
declare type Optional<T> = T | undefined

declare type NotNull<T> = Exclude<T, null>
declare type NotNill<T> = Exclude<T, null | undefined>
declare type Defined<T> = Exclude<T, undefined>

declare type Writable<T> = T extends object ? { -readonly [P in keyof T]: T[P] } : T
