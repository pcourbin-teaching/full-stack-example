export * from './protagonist.service';
import { ProtagonistService } from './protagonist.service';
export * from './quote.service';
import { QuoteService } from './quote.service';
export * from './reference.service';
import { ReferenceService } from './reference.service';
export * from './theme.service';
import { ThemeService } from './theme.service';
export const APIS = [ProtagonistService, QuoteService, ReferenceService, ThemeService];
