/**
 * SPOT API
 * API of SPOT Project
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { Protagonist } from './protagonist';


export interface Reference { 
    id?: number;
    title: string;
    details?: string;
    url?: string;
    date?: string;
    typeID: number;
    typeTitle?: string;
    reliability?: number;
    dateUpdate?: string;
    authors?: Array<Protagonist>;
}
